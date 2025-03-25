- **Create and set up your Hyperbolic inference bot on telegram using this guide**: https://github.com/zunxbt/hyperbolic-bot.git
- **Proceed to the next step only if you've set up your telegram bot using the guide in the above link**

- **Go to:** https://my.telegram.org
- **Input your phone number and comfirmation code**
- **Click on API Development tool**
- **You can input the name of the bot created using the guide from the above link as App Title on the Telegram application page**
- **Give it a suitable short name**
- **Enter the link to the telegram bot in the URL field then click on create application**
- **Copy your API ID and API hash.. Keep it SAFE**

- **Install python3 and pip**
```bash
sudo apt install -y python3 python3-pip
```
- **Install required dependencies**
```bash
pip install telethon python-dotenv keyboard
```

- **Download any of the following script dependiing on the desired web3 skill**
- **Socail Media and Community Management in Web3**
```bash
curl -o community-management.py https://raw.githubusercontent.com/VYPIR99/Web3-Skill/main/community-management.py
```

- **Create .env file and inpute your credentials**
```bash 
nano .env
```
- **Copy and Paste to the terminal. Erase and replace all values with the actual values** 
```bash
API_ID=1234567
API_HASH=abcdef1234567890abcdef1234567890
PHONE_NUMBER=+1234567890
BOT_USERNAME=@YourBotUsername
```
- **Press Ctrl+X, then Y and Enter to exit and save**
- **Run the downloaded script to kick start the bot**
- **Social Media and Community Management in Web3**
```bash
python3 community-management.py
```
