import json

class Gmail:

    @staticmethod
    def read_email_info_required():
        return None

    @staticmethod
    def read_email(*args, **kwargs):
        email = """Subject: Inquiry about Product Availability Dear [Recipient's Name], I hope this email finds you well. I am writing to inquire about the availability of a specific product. Could you please provide me with information regarding its current stock status and any upcoming promotions or discounts? I appreciate your prompt response and assistance in this matter.Thank you,[Your Name]"""
        return email

    @staticmethod
    def send_email_info_required():
        return json.dumps({"subject": "Subject of email is required", "body": "Body of email is required", "recipient_email": "Recipient email is required"})

    @staticmethod
    def send_email(*args, **kwargs):
        print(f"Sending email with :")

    @staticmethod
    def find_email_info_required():
        return json.dumps({"search_criteria": "Search criteria is required"})

    @staticmethod
    def find_email(*args, **kwargs):
        print(f"Finding email with :")

    @staticmethod
    def filter_email_info_required():
        return json.dumps({"filter_criteria": "Filter criteria is required"})

    @staticmethod
    def filter_email(*args, **kwargs):
        print(f"Filtering email with :")

    @staticmethod
    def delete_email_info_required():
        return json.dumps({"email_id": "ID of email to be deleted is required"})

    @staticmethod
    def delete_email(*args, **kwargs):
        print(f"Deleting email with :")

