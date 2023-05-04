from langchain.serpapi import SerpAPIWrapper
from langchain.agents import tool


@tool
def get_profile_url(text: str) -> str:
    """Searches for Linkedin Profile Page."""

    SERPAPI_API_KEY = "b60d6633e64cf905a408e29c4874afb55c106543921ba94615a91c5228da442d"
    search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)
    res = search.run(f"{text}")
    return res
