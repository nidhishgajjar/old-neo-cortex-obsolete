from utils.utilities import Utilities
from tools_store.tools import Tools

class SelectTools:
    def __init__(self, user_input: str, task_pipeline: dict, re_review_data, chat):
        self.chat = chat
        self.tools = Tools().get_tools()
        self.systemprompt = f"""The AI assistant has to consider user input and task to select a suitable tool from a provided list. These tools are designed to process user requests. Below is a list of tools for you to choose from: {self.tools}
            The AI assistant will then output the tool id corresponding to that tool. If there are no suitable tools for the task use ChatGPT tool. Your response MUST be a JSON, with no explanations attached.
            Here's a sample case for reference:
            Sample Input:
            User Input: Read the latest 5 emails and summarize them for me
            [{{"task_id": 0, "task": "Retrieve latest 5 emails"}},
            {{"task_id": 1, "task": "Summarize emails"}}]
            Sample Output:
            [{{"task_id": 0, "tool_id": 57691, "action": "read_email"}},
            {{"task_id": 1, "tool_id": 20984, "action": "create_summary"}}]"""
        if re_review_data:
            self.userprompt = f"{task_pipeline}"
            # print(self.userprompt)
        else:
            self.userprompt = f"User Input: {user_input} {task_pipeline}"

    def select_tools(self) -> dict:      
        response = self.chat.openai_chat([self.chat.role_system(self.systemprompt), self.chat.role_user(self.userprompt)], max_tokens=256)
        print(response)
        json_data = Utilities.extract_json_data(response) # type: ignore
        return json_data