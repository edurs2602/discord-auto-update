# Discord Update Automation Script

This script automates the process of downloading, moving, and extracting a Discord update. It can be useful for users who want to streamline the update process without manual intervention.

## How to Use

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/discord-update-script.git
    cd discord-update-script
    ```

2. **Create a Virtual Environment:**

    Create a Venv for your clone.

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**

    Before running the script, install the required dependencies using:

    ```bash
    pip install requests
    ```

4. **Configure the Script:**

    Open the script (`discord_update_script.py`) in a text editor and update the following variables with your specific information:

    - `discord_update_url`: The URL where the Discord update is hosted.
    - `path`: Create a directory where the discord tar.gz file will be downloaded and extracted.

5. **Run the Script:**

    Execute the script by running:

    ```bash
    python discord_update_script.py
    ```

    The script will download the update, move it to the specified folder, and extract its contents.

6. **Running Alias Example:**
    ```bash
   alias discord='py ~/Documents/Projetos/discord-auto-update/discord_update_script.py; ~/Documents/discord/Discord/Discord'
   ```
   This alias example run the script and after run the discord, maintaining Discord always updated.

## Important Notes

- Ensure that you have Python installed on your system.
- Make sure you have the necessary permissions to perform file operations in the specified download and extract paths.

Feel free to customize the script or contribute improvements by submitting pull requests!

---

**Disclaimer:** Use this script responsibly and in accordance with Discord's terms of service. The script is provided as-is, without any warranties or guarantees.
