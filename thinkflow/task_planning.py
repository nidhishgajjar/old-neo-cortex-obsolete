from utils.utilities import Utilities
from ai import OpenAIChat

class TaskPlanning:
    def __init__(self, user_input: str):
        self.chat = OpenAIChat()
        self.systemprompt = """The AI assistant can parse user input to several tasks: [{"id": "task_id", "task": "task", "dep": "dependency_task_ids"}]. The "dep" field denotes the id of the previous task which generates a new resource that the current task relies on.There is a logical relationship between tasks, please note their order. If the user input can’t be parsed, you need to reply with only an empty {} JSON.
            Here are several cases for your reference:
            User Input: Read the latest 5 emails and summarize them for me
            [{"task_id": "1", "task": "Retrieve latest 5 emails", "dep": []},
            {"task_id": "2", "task": "Summarize emails", "dep": ["1"]}]
            User Input: Email Nidhish about a meeting for tomorrow at 6 pm
            [{"task_id": "1", "task": "Find Nidhish's email", "dep": []},
            {"task_id": "2", "task": "Draft an email", "dep": []},
            {"task_id": "3", "task": "Send email to Nidhish", "dep": ["1", "2"]}]
            User Input: Send a resignation to my boss
            [{"task_id": "1", "task": "Draft resignation letter", "dep": []},
            {"task_id": "2", "task": "Send resignation email to boss", "dep": ["1"]}]."""
        self.userprompt = "User Input: " + user_input

    def tasks(self) -> dict:
        response = self.chat.openai_chat([self.chat.role_system(self.systemprompt), self.chat.role_user(self.userprompt)], max_tokens=256)
        json_data = Utilities.extract_json_data(response) # type: ignore
        return json_data