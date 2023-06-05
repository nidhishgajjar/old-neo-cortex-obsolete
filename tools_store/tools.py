import json
import importlib

tools = [
    {
        "tool_id": 57691,
        "name": "Gmail",
        "description": "An email service provider by Google",
        "action": ["read_email", "send_email", "filter_email", "delete_email"]
    },
    {
        "tool_id": 82103,
        "name": "Email-Drafter",
        "description": "Specifically used for drafting emails",
        "action": ["draft_email"]
    },
    {
        "tool_id": 20984,
        "name": "Summarizer",
        "description": "Specialized in creating a summary of text",
        "action": ["create_summary"]
    },
    {
        "tool_id": 41379,
        "name": "Quick-Search",
        "description": "Quickly search for information on the web",
        "action": ["search_web"]
    },
    {
        "tool_id": 72416,
        "name": "GoogleContacts",
        "description": "A contact management tool by Google",
        "action": ["find_contact_email", "create_contact", "delete_contact"]
    },
    {
        "tool_id": 65742,
        "name": "ChatGPT",
        "description": "Select this tool if no other tool is available for given task",
        "action": ["chat"]
    },
    {
        "tool_id": 39857,
        "name": "Final-Response",
        "description": "Give final response to user",
        "action": ["final_response"]
    }
]

class Tools:
    def __init__(self):
        pass

    def get_tools(self):
        return json.dumps(tools)

    def get_tool_name(self, tool_id):
        for tool in tools:
            if tool["tool_id"] == tool_id:
                return tool["name"] # type: ignore
        return None

    def get_info_required(self, tool_name, action_name):
        # Dynamically import the tool class
        ToolClass = getattr(importlib.import_module(f'tools_store.{tool_name.lower()}'), tool_name)

        # Get the info_required method corresponding to the action
        info_required_method = getattr(ToolClass, f"{action_name}_info_required", None)

        if info_required_method is not None:
            # Call the info_required method
            return info_required_method()
        else:
            print(f"{tool_name} does not have the action {action_name}")
            return None

    def execute_action(self, tool_name, action_name, *args, **kwargs):
        # Dynamically import the tool class
        ToolClass = getattr(importlib.import_module(f'tools_store.{tool_name.lower()}'), tool_name)

        # Get the action method
        action_method = getattr(ToolClass, action_name, None)

        if action_method is not None:
            # Call the action method with any provided arguments
            return action_method(*args, **kwargs)
        else:
            print(f"{tool_name} does not have the action {action_name}")
