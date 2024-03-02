import requests
import os
import shutil
import tarfile

discord_update_url = 'https://discord.com/api/download/stable?platform=linux&format=tar.gz'

# Create a directory where the discord tar.gz file will be downloaded and extracted
path = '/path/to/your/discordDir'


def downloadDiscordToPath(url, path_to_extract):
    with requests.get(url, stream=True) as response:
        with open(path_to_extract, 'wb') as file:
            shutil.copyfileobj(response.raw, file)


def extractArchive(tar_file, path_to_extract):
    with tarfile.open(tar_file, 'r:gz') as tar_ref:
        tar_ref.extractall(path_to_extract)


def main():
    existing_update_file = os.path.join(path, 'discord.tar.gz')

    if os.path.exists(existing_update_file):
        os.remove(existing_update_file)

    try:
        # Download the Discord update
        downloadDiscordToPath(discord_update_url, os.path.join(path, 'discord.tar.gz'))
    except:
        print('Error when download')

    try:
        # Extract the downloaded update
        extractArchive(os.path.join(path, 'discord.tar.gz'), path)
    except:
        print('Error when extract')


if __name__ == "__main__":
    main()
