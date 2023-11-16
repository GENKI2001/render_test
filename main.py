
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

app = Flask(__name__)

# #環境変数取得
line_bot_api = LineBotApi("iT+S9ZKJKWA5xn/a2TPFPEK7dYHCecSIlMLtXrDR7xCsUQlEKWNxk1lIzfOab9LA6pTjNFZvo7yyanZrZLhhPe8RmOJU8D5v7/krgcLz0wqBTA7qDJDzqQ39qFAcJJ3A1eVMgQs4AUt7Ov8bIPubCQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("aed3ff4a3fd4b92220c0d32d1c61c517")
user_id = "U560fe3d60be5ed458afde024c2012d80"


@app.route("/")
def test():
    return "SUCCESS"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'SUCCESS'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.push_message(user_id, messages=TextSendMessage(text=e.message.text))
    

@app.route("/push")
def main():
    line_bot_api.push_message(user_id, messages=TextSendMessage(text="悲しいです...。"))
    return "hello"

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5003))
    app.run(host="0.0.0.0", port=port, debug=True)
