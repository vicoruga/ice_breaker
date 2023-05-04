from langchain.serpapi import SerpAPIWrapper
from langchain.agents import tool


@tool
def get_profile_url(text: str) -> str:
    """Searches for Linkedin Profile Page."""

    SERPAPI_API_KEY = ""
    search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)
    res = search.run(f"{text}")
    return res
