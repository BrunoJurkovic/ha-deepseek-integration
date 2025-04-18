# DeepSeek Integration for Home Assistant

This custom integration for Home Assistant allows you to interact with DeepSeek AI models directly from your smart home.

## Features

- Call DeepSeek AI models from Home Assistant services
- Configure your API key securely through the UI
- Simple service to generate text based on prompts

## Installation

### Manual Installation

1. Copy the `custom_components/deepseek` directory to your Home Assistant `custom_components` directory.
2. Restart Home Assistant.
3. Go to **Configuration** → **Integrations** and click the "+" button.
4. Search for "DeepSeek" and follow the configuration steps.

### HACS Installation (Future)

1. Make sure you have [HACS](https://hacs.xyz/) installed.
2. Go to HACS → Integrations → "Explore & Download Repositories"
3. Search for "DeepSeek" and install it.
4. Restart Home Assistant.
5. Go to **Configuration** → **Integrations** and click the "+" button.
6. Search for "DeepSeek" and follow the configuration steps.

## Configuration

1. You need a DeepSeek API key to use this integration.
2. During setup, enter your API key and optionally specify the model you want to use.
3. The default model is `deepseek-chat`.

## Usage

This integration provides a service called `deepseek.generate_text` that you can call from automations, scripts, or the Developer Tools.

Example service call:

```yaml
service: deepseek.generate_text
data:
  prompt: "Write a short poem about smart homes."
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This project is not affiliated with DeepSeek AI.