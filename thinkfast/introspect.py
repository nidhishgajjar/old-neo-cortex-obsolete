from ai import OpenAIChat

class Introspect:
    def __init__(self, chat):
        self.chat = chat


    def trigger(self, user_input, instinct_response):
        self.systemprompt = f"""Introspect Instincts {instinct_response}"""

        self.userprompt = f"User: {user_input}"
        response = self.chat.openai_chat([self.chat.role_system(self.systemprompt), self.chat.role_user(self.userprompt)], max_tokens=2500)
        return response