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

app = Flask(__name__)

line_bot_api = LineBotApi('2LkA2tNiHWwQTF0q4WZTeEiq4fiEOKwVIDPdA0NboIyfeKY2FGwNq9k1PbyCowKfwT3+1g/CfE+sl5d93cvmYH4oLjVxO7L+iuGRSV1v9I4/+ZiF6oIDFElSNtxuNncgi1nchDc7gKmf4+5PNTW9lAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('79b720c661e74ef28280e09cdf79e967')

@app.route("/test", methods=['GET'])
def test():
    return 'hello'

@app.route("/", methods=['GET'])
def index():
    return 'index'

@app.route("/login", methods=['GET'])
def login():
    return 'login'


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id
    print("user_id =", user_id)
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))



if __name__ == "__main__":
    app.run()