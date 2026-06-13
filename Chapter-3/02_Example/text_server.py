# text_server.py
from mcp.server.fastmcp import FastMCP

text_mcp = FastMCP("Text")


@text_mcp.tool()
def remove_vowels(text: str) -> str:
    """Remove vowels from the given text"""
    vowels = "aeiouAEIOU"
    return ''.join(char for char in text if char not in vowels)


if __name__ == "__main__":
    text_mcp.run(transport="stdio")
