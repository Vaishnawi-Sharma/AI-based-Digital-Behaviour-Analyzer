from ai_utils import classify_with_ai

# classify titles
def classify(title, url):
    text = (str(title) + " " + str(url)).lower()

    if "youtube" in text and "tutorial" in text:
        return "Learning"

    elif "geeksforgeeks" in text or "leetcode" in text:
        return "Learning"

    elif "linkedin" in text or "naukri" in text:
        return "Career"

    elif "instagram" in text or "facebook" in text:
        return "Social Media"

    elif "amazon" in text or "flipkart" in text:
        return "Shopping"

    elif "digilocker" in text or ".gov.in" in text:
        return "Government/Utility"

    elif "netflix" in text or "hotstar" in text:
        return "Entertainment"

    elif "docs.google.com" in text:
        return "Productivity"
    elif "nasscom" in text or "skills" in text:
        return "Career" 
    else:
           return classify_with_ai(title, url)