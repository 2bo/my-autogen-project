import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import os

load_dotenv()

# サンプルツールの定義
async def get_weather(city: str) -> str:
    return f"The weather in {city} is 20 degrees and sunny."

async def main() -> None:
    # エージェントの定義
    weather_agent = AssistantAgent(
        name="weather_agent",
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-mini",
            api_key=os.getenv('OPENAI_API_KEY')
        ),
        tools=[get_weather],
    )

    # タスク終了条件
    termination = TextMentionTermination("TERMINATE")

    # チームの定義
    agent_team = RoundRobinGroupChat([weather_agent], termination_condition=termination)

    # タスクの実行
    stream = agent_team.run_stream(task="What is the weather in Tokyo?")
    await Console(stream)

if __name__ == "__main__":
    asyncio.run(main())
