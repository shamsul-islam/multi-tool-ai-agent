
import os
from tavily import TavilyClient

# It is recommended to set TAVILY_API_KEY as an environment variable
# You can get your key from https://app.tavily.com
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

def medical_web_search(query: str):
    if not TAVILY_API_KEY:
        # Fallback to google_web_search if Tavily API key is not available
        try:
            # This is a placeholder for the actual tool call
            # In a real scenario, you would import and call the tool function
            from agent_tools import google_web_search
            return google_web_search(query)
        except ImportError:
            return "Google web search tool not available."
        except Exception as e:
            return f"An error occurred with Google web search: {e}"

    try:
        client = TavilyClient(api_key=TAVILY_API_KEY)
        response = client.search(query, search_depth="basic")
        return response["results"]
    except Exception as e:
        return f"An error occurred with Tavily search: {e}"

if __name__ == '__main__':
    # Example usage:
    # Make sure to set the TAVILY_API_KEY environment variable before running
    # export TAVILY_API_KEY="your_api_key"
    print(medical_web_search("what are the symptoms of diabetes?"))
