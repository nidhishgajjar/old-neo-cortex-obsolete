class Instinct:
    def __init__(self, user_input, context, chat):
        self.chat = chat
        self.systemprompt = f"""You are an helpful assistant. Context of previous conversation: {context}. Continue the conversation"""

        self.userprompt = f"User: {user_input}"


    def trigger(self):
        print(self.systemprompt)
        response = self.chat.openai_chat([self.chat.role_system(self.systemprompt), self.chat.role_user(self.userprompt)], max_tokens=2500)
        return response