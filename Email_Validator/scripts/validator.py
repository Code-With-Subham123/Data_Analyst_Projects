import re
import pandas as pd

class EmailIntelligence:
    def __init__(self):
        # Professional Regex: Checks format, domain, and common errors
        self.regex = r'^[a-z0-9]([a-z0-9._-]*[a-z0-9])?@[a-z0-9.-]+\.[a-z]{2,7}$'

    def analyze_email(self, email):
        email = str(email).lower().strip()
        is_valid = bool(re.match(self.regex, email))
        
        # Categorizing leads
        category = "Invalid"
        if is_valid:
            if any(domain in email for domain in ["gmail", "yahoo", "outlook", "hotmail"]):
                category = "Personal"
            else:
                category = "Corporate/Professional"
        
        return is_valid, category

    def process_data(self, test_list):
        results = []
        for email in test_list:
            valid, cat = self.analyze_email(email)
            results.append({"Email": email, "Is_Valid": valid, "Type": cat})
        
        df = pd.DataFrame(results)
        print("\n--- Validation Results ---")
        print(df)
        return df

# Initializing and Testing
if __name__ == "__main__":
    tool = EmailIntelligence()
    test_emails = [
        "subham@centurion.edu.in", 
        "invalid..email@gmail", 
        "contact@vito-analytics.com", 
        "user123@yahoo.co.in",
        "wrong-email@.com"
    ]
    tool.process_data(test_emails)