"""The DeepSeek integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from openai import OpenAI, AsyncOpenAI

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

from .const import (
    DOMAIN, 
    CONF_API_KEY, 
    CONF_MODEL,
    CONF_BASE_URL,
    DEFAULT_BASE_URL,
    SERVICE_GENERATE_TEXT,
    ATTR_PROMPT,
    ATTR_RESPONSE
)

_LOGGER = logging.getLogger(__name__)

# Schema for generate_text service
GENERATE_TEXT_SCHEMA = vol.Schema({
    vol.Required(ATTR_PROMPT): cv.string,
})

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the DeepSeek component."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up DeepSeek from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    
    # Store config data in hass.data
    hass.data[DOMAIN][entry.entry_id] = {
        CONF_API_KEY: entry.data[CONF_API_KEY],
        CONF_MODEL: entry.data.get(CONF_MODEL),
        CONF_BASE_URL: entry.data.get(CONF_BASE_URL, DEFAULT_BASE_URL),
    }

    # Register the generate_text service
    async def generate_text(call: ServiceCall) -> None:
        """Handle the generate_text service call."""
        prompt = call.data.get(ATTR_PROMPT)
        api_key = entry.data[CONF_API_KEY]
        model = entry.data.get(CONF_MODEL)
        base_url = entry.data.get(CONF_BASE_URL, DEFAULT_BASE_URL)
        
        try:
            result = await call_deepseek_api(
                api_key=api_key, 
                model=model, 
                prompt=prompt, 
                base_url=base_url
            )
            _LOGGER.debug("DeepSeek response: %s", result)
            
        except Exception as ex:
            _LOGGER.error("Error calling DeepSeek API: %s", ex)
            raise

    hass.services.async_register(
        DOMAIN, 
        SERVICE_GENERATE_TEXT, 
        generate_text, 
        schema=GENERATE_TEXT_SCHEMA
    )

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if hass.data[DOMAIN].get(entry.entry_id) is None:
        return True

    hass.data[DOMAIN].pop(entry.entry_id)
    
    return True

async def call_deepseek_api(
    api_key: str, 
    model: str, 
    prompt: str, 
    base_url: str = DEFAULT_BASE_URL
) -> str:
    """Call DeepSeek API using OpenAI client and return the response."""
    try:
        # Initialize the OpenAI client with DeepSeek's base URL
        client = AsyncOpenAI(
            api_key=api_key,
            base_url=base_url
        )
        
        # Make the API call
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract the response text
        return response.choices[0].message.content
        
    except ImportError as e:
        _LOGGER.error("OpenAI library not found. Install it using pip install openai>=1.0.0")
        raise
    except Exception as e:
        _LOGGER.error("Error calling DeepSeek API: %s", e)
        raise