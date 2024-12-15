FROM python:3.11-slim

# 必要なツールをインストール
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    ffmpeg \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Python環境を準備
RUN pip install --upgrade pip

# ユーザー作成
RUN useradd -ms /bin/bash vscode
USER vscode

# 作業ディレクトリを設定
WORKDIR /workspace
