import logging

from drivers.base_client import BaseClient
from drivers.instagram import InstagramClient


def mute_instagrapi_logger() -> None:
    # Configuring logging to show only errors
    logging.basicConfig(level=logging.ERROR)


def get_social_media_client() -> BaseClient:
    available_options = ['1', '2']
    while True:
        selection = input(
            'Select a social media (enter number):\n1) Instagram\n2) TikTok\n\n> ')
        if selection in available_options:
            break
        print(f"Invalid option. Available options are: {', '.join(available_options)}")

    if selection == '1':
        return InstagramClient()
    else:
        print('TikTok is still in progress.')
        return None


def main():
    mute_instagrapi_logger()
    client = get_social_media_client()

    if client:
        client.block_users()


if __name__ == "__main__":
    main()
