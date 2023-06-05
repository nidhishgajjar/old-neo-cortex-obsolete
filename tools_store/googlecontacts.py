import json

class GoogleContacts:

    @staticmethod
    def find_contact_email_info_required():
        return json.dumps({"name": "contact name is required"})

    @staticmethod
    def find_contact_email(*args, **kwargs):
        return "Ask and Chat with user"