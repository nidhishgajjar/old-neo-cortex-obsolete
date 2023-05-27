import json
import re

class Utilities:
    def __init__(self):
        # Initialize instance variables here if needed
        pass
    
    @staticmethod
    def extract_json_data(response: str) -> dict:
        try:
            # Extract JSON string from the response using a regular expression
            json_string = re.search(r'(\[.*\])|(\{.*\})', response, re.DOTALL).group() # type: ignore
            
            # Load the JSON string into a Python object
            json_data = json.loads(json_string)
            
            # Return the Python object
            return json_data
        except json.JSONDecodeError:
            print("The response is not a valid JSON string.")
            return {}
        except AttributeError:
            print("No JSON data found in the response.")
            return {}
        
    @staticmethod
    def get_current_task_details(task_pipeline, selected_tools):
        current_task = task_pipeline[0]
        task_id = current_task["task_id"]
        for tool in selected_tools:
            if tool["task_id"] == task_id:
                return {
                    "task_id": task_id,
                    "current_task": current_task["task"],
                    "tool_id": tool["tool_id"],
                    "action": tool["action"]
                }
        return None