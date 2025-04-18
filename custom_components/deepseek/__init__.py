"""The DeepSeek integration."""
from __future__ import annotations

import logging
import aiohttp
import async_timeout
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

from .const import (
    DOMAIN, 
    CONF_API_KEY, 
    CONF_MODEL,
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
    }

    # Register the generate_text service
    async def generate_text(call: ServiceCall) -> None:
        """Handle the generate_text service call."""
        prompt = call.data.get(ATTR_PROMPT)
        api_key = entry.data[CONF_API_KEY]
        model = entry.data.get(CONF_MODEL)
        
        try:
            # TODO: Replace with actual DeepSeek API call
            result = await call_deepseek_api(hass, api_key, model, prompt)
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
    hass: HomeAssistant, api_key: str, model: str, prompt: str
) -> str:
    """Call DeepSeek API and return the response."""
    # This is a placeholder. Replace with actual DeepSeek API implementation
    try:
        # To be replaced with actual DeepSeek client library
        import deepseek
        
        # Initialize the client with the API key
        client = deepseek.Client(api_key=api_key)
        
        # Make the API call
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract the response text
        return response.choices[0].message.content
        
    except ImportError:
        _LOGGER.error("DeepSeek library not found. Install it using pip install deepseek-ai")
        raise
    except Exception as ex:
        _LOGGER.error("Error calling DeepSeek API: %s", ex)
        raise