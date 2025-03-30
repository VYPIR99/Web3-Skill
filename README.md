- This bot is meant to assist web3 ethusiast with or without any knowledge of coding or programming learn valuable skill(s) in web3 utilizing any of the inferencing models available on Hyperbolic AI. 6 important areas have been identified:
1. Social Media and Community Management
2. Content Creation and Writing,
3. Web3 Community Education & Onboarding
4. Marketing & Business Development
5. Research & Analysis
6. NFT & Digital Art Creation

- This bot automatically send a question from your telegram account to the hyperbolic telegram bot you created every 100 seconds. The hyperbolic inference model selected (DEEPSEEK V3 recommended) provides answers to these questions, typically in less than 20 seconds. There are 50 questions (10 questions in 5 sets) in total for each skill. The first set of questions are basic and introductory. Subsequent questions tends to be more technical, and help build and expand on the knowledge gained from prior question to ensure a favourable learning curve.

- After each set of question (i.e 10 question), there will be an interval of 3 hours before the next set of question starts sending. This is to enable the learner, research and understand more on any aspect or answer that is not clear. The bot also can be paused, resumed, and restarted at anytime by the learner.

- It is recommended to run this bot using the terminal on your local linux server as uploading your API ID to a VPS renders your telegram account vulnerable. However, if you should prefer using a vps, it is suggested you create a new telegram account or use a burner telegram account that contains no sensitive info for security reasons.




- **STEPS TO SETTING UP THE BOT**

- **Create and set up your Hyperbolic inference bot on telegram using this guide**: https://github.com/zunxbt/hyperbolic-bot.git
- **Proceed to the next step only if you've set up your telegram bot using the guide in the above link. If you haven't go set up the Hyperbolic bot first, then return and proceed to the next step**

- **Go to:** https://my.telegram.org
- **Input your phone number and comfirmation code**
- **Click on API Development tool**
- **You can input the name of the bot created using the guide from the above link as App Title on the Telegram application page**
- **Give it a suitable short name**
- **Enter the link to the telegram bot in the URL field then click on create application**
- **Copy your API ID and API hash.. Keep it SAFE**
- **Go to the hyperbolic bot you created on telegram, select "Text Models" then "DEEPSEEK V3"**
- **ON YOUR SERVER**
- **Install python3 and pip**
```bash
sudo apt install -y python3 python3-pip
```
- **Install required dependencies**
```bash
pip install telethon python-dotenv keyboard
```

- **Download any of the following script dependiing on the desired web3 skill**
- **Social Media and Community Management in Web3**
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

- **Let's run the downloaded script to start the bot**
- **Social Media and Community Management in Web3**
- **Create a screen session**
```bash
screen -S community-management
```
- **START THE BOT**
```bash
python3 community-management.py
```

- **The first time you run the script, you will be asked to input a verification code, which will be sent to your Telegram.**
- **Enter the code to authenticate.**
- **After this, session details will be stored and you won’t need to log in again.**
- **While in Screen, Press P to pause the bot, and R to resume.**

- **Press Ctrl+C to stop the bot or Ctrl+A+D to minimize the screen**

- **Use this command to return to the screen**
```bash
screen -r community-management
```
