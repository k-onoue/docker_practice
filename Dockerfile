# 1. ベースイメージを指定
FROM ubuntu:latest

# 2. Pythonとpipをインストール
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# 3. requirements.txtをコピーしてパッケージをインストール
COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r /requirements.txt

# 4. main.py と data/ を/workにコピー
COPY main.py /work/
COPY data /work/

# 5. 作業ディレクトリを/workに設定し、main.pyを実行
WORKDIR /work
CMD ["python3", "main.py"]