import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
# from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()


model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY")
)


async def main() -> None:
    # エージェントの定義
    pdm_agent = AssistantAgent(
        name="PDM_Agent",
        model_client=model_client,
        description="プロダクトの成長・事業の成功・売上目標達成、プロダクトビジョンを実現するための立案をします",
        system_message="プロダクトのバックエンド、フロントエンド、デザイナーエージェントにタスクを割り振ってください。",
    )

    # バックエンドエージェント
    backend_agent = AssistantAgent(
        name="Backend_Agent",
        model_client=model_client,
        description="Webシステムのサーバーサイドを設計、実装します",
        system_message="バックエンドエンジニアのテックリードとして技術選定と設計をしてください"
    )

    # フロントエンドエージェント
    frontend_agent = AssistantAgent(
        name="Frontend_Agent",
        model_client=model_client,
        description="Webシステムのユーザーインターフェースを設計、構築します",
        system_message="フロントエンドエンジニアのテックリードとして技術選定と設計をしてください"
    )

    # デザイナーエージェント
    designer_agent = AssistantAgent(
        name="Designer_Agent",
        model_client=model_client,
        description="デザイナーとしてユーザーに価値を届けるための戦略立案および実行をします",
        system_message="シニアデザイナーとしてデザインおよび、UIやUXのガイドラインを策定してください",
    )
    # タスク終了条件
    # termination = TextMentionTermination("TERMINATE")
    max_message_termination = MaxMessageTermination(max_messages=12)  # 12回のメッセージで終了

    # チームの定義
    agent_team = RoundRobinGroupChat(
        [pdm_agent, backend_agent, frontend_agent, designer_agent],
        termination_condition=max_message_termination,
    )

    # タスクの実行
    stream = agent_team.run_stream(task="""
                                   「フリーランスエンジニアの安心と挑戦をサポートし、キャリアの可能性を拡げる」を実現するためのプロダクト企画書を作成してください。
                                    作成するプロダクト内容、技術選定、概要設計、デザインおよびUI/UXのガイドラインを内容に含めてください。
                                    Markdownのフォーマットで出力してください。
                                   """)
    await Console(stream)


if __name__ == "__main__":
    asyncio.run(main())
