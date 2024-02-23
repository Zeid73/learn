# logging.basicConfig(
#     format="%(message)s %(asctime)s",
#     datefmt="%Y/%m/%d %I:%M:%S %p",
#     level=logging.INFO,
#     filename="py_log.log",
#     filemode="a",
# )


import json
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("t1.log")
file_formatter = logging.Formatter("{'timestamp':'%(asctime)s','data': '%(message)s'}")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

username = "usernccame"
user_id = "id"
chat_id = "chatid"
chat_type = "chat type"
text = "text"

data = {
    "user_id": f"{username}",
    "username": f"{username}",
    "message_type": f"{chat_type}",
    "chat_id": f"{chat_id}",
    "message": f"{text}",
}
logging.disable(logging.INFO)

logging.disable(logging.NOTSET)
logging.info(json.dumps(data))
logging.disable(logging.INFO)
