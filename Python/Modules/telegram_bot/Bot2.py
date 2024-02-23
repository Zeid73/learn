# token = ""
# bot_username = "@Z1873bot"

# import requests

# TOKEN = ""
# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# print(requests.get(url).json())

# # 840262200

# # TOKEN = "YOUR TELEGRAM BOT TOKEN"
# chat_id = 840262200
# message = "hello from your telegram bot"
# url = (
#     f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
# )
# print(requests.get(url).json())


# message = "Access denied"
# url = (
#     f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
# )
# print(requests.get(url).json())

import requests
from logging import Handler, Formatter
import logging
import datetime

TELEGRAM_TOKEN = ""
TELEGRAM_CHAT_ID = ""


class RequestsHandler(Handler):
    def emit(self, record):
        log_entry = self.format(record)
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": log_entry, "parse_mode": "HTML"}
        return requests.post(
            "https://api.telegram.org/bot{token}/sendMessage".format(
                token=TELEGRAM_TOKEN
            ),
            data=payload,
        ).content


class LogstashFormatter(Formatter):
    def __init__(self):
        super(LogstashFormatter, self).__init__()

    def format(self, record):
        t = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        return "<i>{datetime}</i><pre>\n{message}</pre>".format(
            message=record.msg, datetime=t
        )


def main():
    logger = logging.getLogger("trymeApp")
    logger.setLevel(logging.WARNING)

    handler = RequestsHandler()
    formatter = LogstashFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.setLevel(logging.WARNING)

    logger.error("We have a problem")


if __name__ == "__main__":
    main()
