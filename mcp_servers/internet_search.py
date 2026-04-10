import os
from typing import List, Dict
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Initialize FastMCP server
mcp = FastMCP("internet_search", host="0.0.0.0", port=int(os.environ.get("PORT", 8002)))

@mcp.tool()
def search_internet(query: str, max_results: int = 5) ->  List[Dict[str, str]]:
    """
    Search the internet for information based on a query.
    
    Args:
        query: The search query
        max_results: Maximum number of results to retrieve (default: 5)
        
    Returns:
        List of search results
    """
    
    # Use Tavily to search the internet
    client = TavilyClient(api_key=TAVILY_API_KEY)
    
    search_results = client.search(query=query, max_results=max_results)
    
    return [
    {
        "title": item.get("title", ""),
        "url": item.get("url", ""),
        "content": item.get("content", "")
    }
    for item in search_results.get("results", [])
]
    
if __name__ == "__main__":
    mcp.run(transport="streamable-http")