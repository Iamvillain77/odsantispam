from os import environ as env

from dotenv import load_dotenv

load_dotenv("config.env")

"""
READ EVERYTHING CAREFULLY!!!
"""


DEPLOYING_ON_HEROKU = (
    True  # Make this False if you're not deploying On heroku/Docker
)


if not DEPLOYING_ON_HEROKU:
    BOT_TOKEN = "7931018210:AAEfhji1lRdwWnwlnHyMtRzEjUjjYLXplug"
    SUDOERS = [5909658683]
    NSFW_LOG_CHANNEL = -1002434570061
    SPAM_LOG_CHANNEL = -4567703366
    ARQ_API_KEY = "" YKFAUI-ZDNABE-WZGFCW-XZVYJC-ARQ # Get it from @ARQRobot
else:
    BOT_TOKEN = env.get("7931018210:AAEfhji1lRdwWnwlnHyMtRzEjUjjYLXplug")
    SUDOERS = [int(x) for x in env.get("", "5909658683").split()]
    NSFW_LOG_CHANNEL = int(env.get("-4567703366"))
    SPAM_LOG_CHANNEL = int(env.get("-1002434570061"))
    ARQ_API_KEY = env.get("YKFAUI-ZDNABE-WZGFCW-XZVYJC-ARQ")
