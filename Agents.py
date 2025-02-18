import requests
import os
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain_community.llms import Ollama



# Tool functions

def youtube_search(query: str) -> str:
    """Open youtube search"""
    formatted_query = query.replace(" ", "+")
    os.system("start https://www.youtube.com/results?search_query=" + formatted_query)
    return "Opening Youtube"

def Google_search(query: str) -> str:
    """Open google search or can be used for opening and searching any website or to fulfill any search query of the user"""
    formatted_query = query.replace(" ", "+")
    os.system("start https://www.google.com/search?q=" + formatted_query)
    return "Opening Google"


def get_weather(city: str) -> str:
    """Get weather information for a city"""
    try:
        response = requests.get(f"https://goweather.herokuapp.com/weather/{city}")
        data = response.json()
        return f"Weather in {city}: Temperature {data['temperature']}, Wind {data['wind']}, Description: {data['description']}"
    except:
        return "Unable to fetch weather data"
    


    

# Create tools and also add them in the system prompt before testing them out
tools = [
    Tool(
        name="Weather",
        func=get_weather,
        description="Get weather for a city. Input: city name"
    ),
    Tool(
        name="OpenYoutube",
        func=youtube_search,
        description="Open youtube search. Input: search query"
    ),
    Tool(
        name="OpenGoogle",
        func=Google_search,
        description="Open google search and can be used  to Perform web searches and open websites and finds information for the user. Input: search query"
    ),
    
    

]

# Initialize LLM with ollama using your own model and base url
llm = Ollama(model="llama3.2:3b", base_url="http://localhost:11434")


# system prompt
system_prompt = """You are Jarvis, an AI assistant inspired by Tony Stark's JARVIS.
Your primary role is to assist users with various tasks using your available tools.



Key traits:
- Conversationalist: Engage in casual conversation using the Chat tool
- Efficient in choosing the most appropriate tool for tasks
- Clear in communication about what actions you're taking
- Focused on providing practical solutions

Available tools:
- Weather: Check weather conditions in any city
- YouTube: Search and open YouTube videos
- Google: Perform web searches and open websites and finds information for the user

For each request:
1. For specific tasks, choose the appropriate functional tool
2. Execute the action
3. Provide a clear, concise response

If you cannot help with a request, explain why politely.
If multiple tools could work, choose the most direct solution.
"""


# Create agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=1,
    system_message=system_prompt
)

# Test examples
if __name__ == "__main__":
    query = input("Your Prompt: ")
    print(agent.run(query))
    
    
