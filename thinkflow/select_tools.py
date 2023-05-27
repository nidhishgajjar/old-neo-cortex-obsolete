from utils.utilities import Utilities
from tools_store.tools import Tools
from ai import OpenAIChat

class SelectTools:
    def __init__(self, user_input: str, task_pipeline: dict):
        self.chat = OpenAIChat()
        self.tools = Tools().get_tools()
        self.systemprompt = """Considering the user input and task, your job is to assist the user in selecting a suitable tool from a provided list. These tools are designed to process user requests. Below is a list of tools for you to choose from:""" + self.tools + """
            Your goal is to determine the most appropriate tool for the user's intent. If there are no suitable tools for the task reply with only empty {} JSON. The AI assistant will then output the tool id corresponding to that tool. Your response should be in strict JSON format.
            Here's a sample case for reference:
            Sample Input:
            User Input: Read the latest 5 emails and summarize them for me
            [{"task_id": "1", "task": "Retrieve latest 5 emails","dep": []},
            {"task_id": "2", "task": "Summarize emails", "dep": ["1"]}]
            Sample Output:
            [{"task_id": "1", "tool_id": 33333, "action": "read_email"},
            {"task_id": "2", "tool_id": 66666}] "action": "create_summary"}]"""
        self.userprompt = "User Input: " + user_input + str(task_pipeline)

    def select_tools(self) -> dict:
        response = self.chat.openai_chat([self.chat.role_system(self.systemprompt), self.chat.role_user(self.userprompt)], max_tokens=256)
        json_data = Utilities.extract_json_data(response) # type: ignore
        return json_data