import time
import os
from dotenv import load_dotenv
from telethon import TelegramClient

# Load environment variables from .env file
load_dotenv()

API_ID = int(os.getenv("API_ID"))  # Convert to integer
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
BOT_USERNAME = os.getenv("BOT_USERNAME")

# List of questions
questions = [
    "What is community management in Web3?",
    "How is Web3 community management different from Web2?",
    "What are the key roles of a Web3 community manager?",
    "Why is community engagement important for a Web3 project?",
    "Which platforms are most commonly used for Web3 communities?",
    "How do Telegram and Discord differ in community management?",
    "What are the essential tools for managing a Web3 community?",
    "How do I choose the right social media channels for a Web3 project?",
    "What are some examples of successful Web3 communities?",
    "What are the best practices for onboarding new members into a Web3 community?",
    
    "How can I grow an engaged Web3 community from scratch?",
    "What type of content works best for Web3 community engagement?",
    "How do I handle spam and scams in a Web3 community?",
    "What strategies can I use to increase member retention?",
    "How can I encourage community members to contribute actively?",
    "What are the key elements of a strong community culture?",
    "How can I measure the success of a Web3 community?",
    "What is the role of governance in Web3 communities?",
    "How do I manage FUD (Fear, Uncertainty, and Doubt) in a community?",
    "How do DAOs (Decentralized Autonomous Organizations) impact community management?",
    
    "What are some ways to incentivize community participation?",
    "How can I create and manage a rewards system for community engagement?",
    "What are the legal and ethical considerations in Web3 community management?",
    "How can I leverage influencers and ambassadors in Web3 marketing?",
    "What are some automation tools for managing a large Web3 community?",
    "How do I plan and execute a successful community event or AMA (Ask Me Anything) session?",
    "How can I integrate NFTs and tokens into community engagement strategies?",
    "What are some common mistakes to avoid in Web3 community management?",
    "How do I handle community conflicts and disputes?",
    "How can I structure a Web3 community for long-term sustainability?",
    
    "How do I create an effective Web3 community engagement roadmap?",
    "How can I optimize Twitter Spaces and Discord stages for community engagement?",
    "What are the best practices for managing multi-language Web3 communities?",
    "How do I use analytics to improve community growth and engagement?",
    "How do I create partnerships between Web3 communities?",
    "What are some innovative ways to gamify Web3 communities?",
    "How do I balance decentralization and moderation in a Web3 community?",
    "What are some strategies for transitioning a Web2 community into Web3?",
    "How do I manage a crisis or PR issue in a Web3 community?",
    "What are the future trends in Web3 community management?",
    
    "How can I become a Web3 community manager with no prior experience?",
    "What skills do I need to develop to excel in Web3 community management?",
    "How can I build my personal brand as a Web3 community manager?",
    "What are some recommended courses or resources for learning Web3 community management?",
    "How can I get my first job or gig in Web3 community management?",
    "What are the salary expectations for Web3 community managers?",
    "How do I network with other Web3 professionals?",
    "How can I transition from Web3 community management into other Web3 roles?",
    "How can I stay updated with the latest trends in Web3 communities?",
    "What are the biggest challenges Web3 community managers face today?"
]

# Initialize the Telegram client
client = TelegramClient("session_name", API_ID, API_HASH)

async def send_questions():
    await client.start(PHONE_NUMBER)  # Log in if not already logged in

    for index, question in enumerate(questions):
        await client.send_message(BOT_USERNAME, f"Q{index + 1}: {question}")
        print(f"Sent Question {index + 1}: {question}")

        # Pause for 100 seconds after each question
        if index < len(questions) - 1:
            if (index + 1) % 10 == 0:
                print("Pausing for 3 hours before sending the next batch of questions...")
                time.sleep(3 * 60 * 60)  # 3-hour pause after every 10th question
            else:
                time.sleep(100)  # Wait for 100 seconds before sending the next question

# Run the script
with client:
    client.loop.run_until_complete(send_questions())
