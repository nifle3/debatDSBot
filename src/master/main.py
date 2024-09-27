import os
from sys import exit

from dotenv import load_dotenv

from bot import bot

load_dotenv()


def main():
    bot_token = os.environ.get("DISCORD_TOKEN")
    if bot_token is None:
        print_error("Bot token is not define")
        exit(1)

    bot.run(bot_token)


def print_error(error: str):
    print(f"\u001b[31m{error}\u001b[0m")


if __name__ == "__main__":
    main()
