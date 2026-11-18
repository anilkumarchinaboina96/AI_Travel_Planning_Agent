from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def tavily_search(query):
    response = client.search(query, max_results=5)
    result = []

    for i, r in enumerate(response["results"],1):
        title = r.get("title", "unknown")
        url = r.get("url", "")
        snippet = r.get("snippet", "").strip()
        if len(snippet) > 300:
            snippet = snippet[300:].rsplit(" ",1)[0] + "..."
        result.append(f"{i}. **{title}**\n{url}\n{snippet}\n")
    return "\n\n".join(result)