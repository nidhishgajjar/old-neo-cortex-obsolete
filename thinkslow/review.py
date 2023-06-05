from utils.utilities import Utilities
from tools_store.tools import Tools

class Review:
    def __init__(self, review_data: list, info_required: list, current_task, chat):
        self.chat = chat
        self.tools = Tools().get_tools()
        self.systemprompt = f"""The AI assistant has to find the required information inside the given data: Given Data: {review_data}
            If required information can be found inside the given data then parse that into the following JSON 
            {{"have_all_required_inputs": true, "key_from_required_information": "key_with_value"}} where key_with_value is the key that contains required information.
            Conversely, if the information isn't present, the assistant must generate a new task which precedes the current task. 
            This new task will aim at obtaining the missing information for the current task (current task: {current_task}), and will be returned in the JSON format: {{"have_all_required_inputs": false, "new_task": "new_task"}}.
            Your response MUST be a JSON, with no explanations attached.
            Here are few examples for your reference: Example 1: Given Data: {{"user_input": "Send an email about my wedding to Nidhish"}}, {{"prev_outcomes":{{"find_email":"nidhish@gmail.com"}}}}
            Information Required: {{"email_id": "email address"}}
            Sample Output: [{{"have_all_required_inputs": true, "email_id": "find_email"}}]
            Example 2: Given Data: {{"user_input": "Find latest email recieved from Nidhish"}}
            Information Required: {{"email_id": "email address"}}
            Sample Output: [{{"have_all_required_inputs": false, "new_task": "Find Nidhish's email"}}]"""

        self.userprompt = f"Required Information: {info_required}"


    def review_info(self) -> dict:
        response = self.chat.openai_chat([self.chat.role_system(self.systemprompt), self.chat.role_user(self.userprompt)], max_tokens=256)
        print("Review Info Response: ")
        print(response)
        json_data = Utilities.extract_json_data(response) # type: ignore

        return json_data