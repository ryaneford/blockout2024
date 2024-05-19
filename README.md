# BlockOut2024

Automated script for blocking celebrities on Instagram.

## Prerequisites

1. **Install Python 3.7+**:
    - Download from [python.org](https://www.python.org/downloads/) and follow the installation instructions.
    - Ensure `pip` is installed.

2. **Install Git**:
    - Download from [git-scm.com](https://git-scm.com/downloads) and follow the installation instructions.

## Setup Instructions

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/ryaneford/blockout2024.git
    cd blockout2024
    ```

2. **Set Up a Virtual Environment** (Optional but Recommended):
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    - Ensure `pip` is up to date:
        ```sh
        pip install --upgrade pip
        ```
    - Install required packages:
        ```sh
        pip install -r requirements.txt
        ```

4. **Prepare Instagram Credentials**:
    - Create `credentials.txt` in the root directory with the following content:
        ```
        username:your_instagram_username
        password:your_instagram_password
        ```

5. **Run the Script**:
    ```sh
    python3 main.py
    ```

## Two-Factor Authentication (2FA)

- If your Instagram account has 2FA enabled, the script will prompt you to enter the 2FA code after providing your username and password.
- Ensure you have access to your 2FA method (e.g., authentication app, SMS) when running the script.

-  ### Usage example

![example.jpeg](resources/example.jpeg)

The list of usernames that will be blocked when executed are:

- `resources/usernames/instagram.txt` for Instagram 

## Notes

- The script reads credentials from `credentials.txt` and logs in to your Instagram account.
- Follow the on-screen prompts to block specified users.
- Ensure paths in the script match your project's directory structure if modified.

For more information, visit the [BlockOut2024 GitHub repository](https://github.com/ryaneford/blockout2024).

