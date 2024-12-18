# My Autogen Project

このプロジェクトは、`Autogen`と`Autogen Studio`を使用してマルチAIエージェントを構築するサンプルです。

## Requirements

- Visual Studio Code
   - Dev Containers Extension
- Docker

## Setup

Visual Studio Codeでプロジェクトを開き、Devcontainerを起動します

## Autogen Studioの起動

Devcontainerのターミナルで以下を実行します

```sh
$ autogenstudio ui --host 0.0.0.0 --port 8080 --appdir /workspace/data
```

ブラウザで`http://localhost:8080`を開きます

## Augogenの実行

OPENAI APIのキーを発行します。
.envファイルを作成し、OPENAI_API_KEYに発行したキーを設定します

```bash 
$ cp .env.sample .env
```

Devcontainerのターミナルでmain.pyを実行します

```bash
$ python main.py
```
