
# Multi-Tool AI Agent for Medical Datasets

This project is a multi-tool AI agent that can answer questions about medical datasets and general medical knowledge.

## Project Structure

- `main.py`: The main script to run the AI agent.
- `create_databases.py`: Script to create SQLite databases from CSV files.
- `database_tools.py`: Contains functions to query the medical databases.
- `web_search_tool.py`: Contains the function for web searches.
- `requirements.txt`: Lists the required Python libraries.
- `heart.csv`, `cancer.csv`, `diabetes.csv`: The raw data files.
- `heart_disease.db`, `cancer.db`, `diabetes.db`: The SQLite databases.

## Setup

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Set API Key:**

   This project uses the Tavily API for web searches. You need to get an API key from [Tavily](https://app.tavily.com/).

   Set the `TAVILY_API_KEY` environment variable:

   ```bash
   export TAVILY_API_KEY="your_tavily_api_key"
   ```

3. **Create Databases:**

   Run the following script to create the SQLite databases from the CSV files:

   ```bash
   python create_databases.py
   ```

## How to Run the Agent

Once you have completed the setup, you can run the AI agent:

```bash
python main.py
```

The agent will then prompt you to ask a medical question.

## Google Colab Instructions

1. Upload the entire project folder to your Google Drive.
2. Open the `main.py` file in Google Colab.
3. Make sure to set the `TAVILY_API_KEY` in the Colab environment.
4. You can run the setup steps in Colab cells.
