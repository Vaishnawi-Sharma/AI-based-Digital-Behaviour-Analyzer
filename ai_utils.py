
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("API KEY NOT FOUND")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")


def classify_with_ai(title, url):
    prompt = f"""
Classify this browser page into ONLY one category:

Learning
Career
Productivity
Social Media
Entertainment
Utility
Shopping
Unknown

Title: {title}
URL: {url}

Return only category name.
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        print("CLASSIFY ERROR:", e)
        return "Unknown"


def generate_summary(stats_text):
    prompt = f"""
Analyze this browser activity summary and give 3 short professional lines.

{stats_text}
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        print("SUMMARY ERROR:", e)
        return "User shows mixed browsing behavior with productive and neutral activity."