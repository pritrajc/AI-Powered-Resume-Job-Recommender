# AI-Powered Resume & Job Recommender

Analyze a resume with a locally running Ollama model and discover relevant job
listings on LinkedIn and Naukri.

Upload a PDF resume to receive an AI-generated resume summary, skill-gap
analysis, and career roadmap. The app then derives job-search keywords from the
summary and fetches up to five listings from each job source.

## Features

- Extracts text from PDF resumes.
- Uses a local Ollama model to summarize experience, identify skill gaps, and
  suggest a career roadmap.
- Searches LinkedIn and Naukri through Apify actors, showing up to five results
  from each.
- Provides a Streamlit web interface.

## Requirements

- Python 3.10 or newer
- [Ollama](https://ollama.com/) installed and running locally
- An [Apify](https://apify.com/) API token for job searches

## Setup

1. Install the Ollama model:

   ```powershell
   ollama pull qwen2.5:3b
   ```

2. Create a local environment file and add your Apify token:

   ```powershell
   Copy-Item .env.example .env
   ```

   Set `APIFY_API_TOKEN` in `.env`. The Ollama URL and model have local defaults;
   change `OLLAMA_BASE_URL` or `OLLAMA_MODEL` there if needed.

3. Install dependencies and start the app:

   ```powershell
   pip install -r requirement.txt
   streamlit run app.py
   ```

The resume analysis runs against the local Ollama server at
`http://localhost:11434/v1` by default. No OpenAI API key is required.

## Configuration

| Variable | Purpose | Default |
| --- | --- | --- |
| `APIFY_API_TOKEN` | Authenticates job searches through Apify | None; required for job search |
| `OLLAMA_BASE_URL` | Ollama OpenAI-compatible API endpoint | `http://localhost:11434/v1` |
| `OLLAMA_MODEL` | Local model name installed in Ollama | `qwen2.5:3b` |

Keep credentials in `.env`. Do not commit `.env` or paste API tokens into source
code; `.env` is excluded by `.gitignore`.
