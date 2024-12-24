# web2llm-webui

A simple yet powerful tool to use LLM (Large Language Models) into advanced AI web scrapers. This project leverages the capabilities of the open-source libraries [Ollama](https://ollama.ai/) and [ScrapeAI](https://scrapeai.com/) to deliver seamless integration and functionality.

## Features

- **Interactive Web Interface**: Quickly convert your LLM-powered applications into a user-friendly web UI.
- **Powered by Open-Source**: Built with [Ollama](https://ollama.ai/) for LLM processing and [ScrapeAI](https://scrapeai.com/) for enhanced data extraction and integration.
- **Customizable and Extensible**: Designed with developers in mind, allowing easy customization and scaling.

## How It Works

1. **Backend Integration**: llm2webui connects your LLM model through Ollama to handle language processing.
2. **Data Extraction**: ScrapeAI provides robust data scraping and parsing for dynamic content needs.
3. **Frontend Generation**: A clean, intuitive web interface is automatically generated to interact with your LLM.

## Getting Started

### Prerequisites

- Node.js and npm installed
- Python 3.8 or higher
- Ollama and ScrapeAI installed (see their respective documentation)

### Installation
It's advised to install this repo in a venv

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/llm2webui.git
   cd llm2webui

2. Install dependencies
   ```bash
   npm install
   pip install -r requirements.txt

3. Configure your API keys. Add them to the .env file:
   OpenAI-API is optional, Ollama will work out of the box.
   ```env
   OPENAI_API_KEY=your_ollama_api_key

#### Running the tool

Run the start_webui.py
```python
python start_webui.py
```

Acces the web interface in your browser at:
```url
http://localhost:8188
```
