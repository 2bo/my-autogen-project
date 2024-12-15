# My Autogen Project

このプロジェクトは、`autogen`を使用してマルチAIエージェントを構築するサンプルです。

## Requirements

- Visual Studio Code
 - Dev Containers Extension
- Docker

## Setup

### 1 .envの設定
  ```bash 
  $ cp .env.sample .env
  ```
  OPENAI APIのキーを発行し、OPENAI_API_KEYに設定します

### 2. Dev Containerの起動

## Autogen Studioの起動

devcontainerのターミナルで以下を実行します

```sh
$ autogenstudio ui --host 0.0.0.0 --port 8080 --appdir /workspace/data
```

ブラウザで`http://localhost:8080`を開きます
