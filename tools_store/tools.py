import json

tools = [
    {
        "tool_id": 57691,
        "name": "Gmail",
        "description": "An email service provider by Google",
        "action": ["create_email", "read_email", "send_email", "find_email", "filter_email", "delete_email"]
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
        "name": "Google-Contacts",
        "description": "A contact management tool by Google",
        "action": ["find_contact_email", "create_contact", "delete_contact"]
    },
    {
        "tool_id": 65742,
        "name": "General",
        "description": "Everything tool only use this tool when no other tool is applicable",
        "action": ["chat"]
    },
    {
        "tool_id": 39857,
        "name": "Final-Response",
        "description": "Give final response to user",
        "tool_intents": ["final_response"]
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
                return tool["name"]
        return None