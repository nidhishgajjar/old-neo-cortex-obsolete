# from tools_store import Tools
# from thinkflow.review import Review
# from thinkflow.select_tools import SelectTools
# from utils.utilities import Utilities


# class TaskExecutor:
#     def __init__(self, user_input, tasks_pipeline, current_task_details, selected_tools):
#         self.user_input = user_input
#         self.tasks_pipeline = tasks_pipeline
#         self.selected_tools = selected_tools
#         self.current_task_details = current_task_details
#         self.prev_outcomes = {}
#         self.review_data = []

#     def executor(self):
#         tools = Tools()
#         self.current_task_details = Utilities.get_current_task_details(self.tasks_pipeline, self.selected_tools)
#         if self.current_task_details is None:
#             print("Error: No current task details found")
#             return True

#         if self.current_task_details["action"] == "final_response":
#             print("Final response")
#             return True

#         self.current_tool_id = self.current_task_details["tool_id"]
#         self.current_tool_name = tools.get_tool_name(self.current_tool_id)
#         self.current_tool_action = self.current_task_details["action"]

#         info_required = tools.get_info_required(self.current_tool_name, self.current_tool_action)
#         print("Info required")
#         print(info_required)
#         if info_required is None:
#             outcome = tools.execute_action(self.current_tool_name, self.current_tool_action)
#             self.prev_outcomes[self.current_tool_action] = outcome
#             self.tasks_pipeline.pop(0)
#             return False

#         self.review_data.append({
#             "user_input": self.user_input,
#             "prev_outcomes": self.prev_outcomes})
        
#         # print("Review data")
#         # print(self.review_data)
        
#         review = Review(self.review_data, info_required, self.current_task_details["current_task"])
#         findings = review.review_info()

#         if not findings["have_all_required_inputs"]:
#             new_task_id = len(self.tasks_pipeline)
#             self.tasks_pipeline.insert(0, {"task_id": new_task_id, "task": findings["new_task"]})
#             find_tools = SelectTools(self.user_input, self.tasks_pipeline[0], True)
#             new_selected_tools = find_tools.select_tools()
            
#             # print(new_selected_tools)
            
#             # Ensure selected_tools is a list
#             if isinstance(new_selected_tools, dict):
#                 new_selected_tools = [new_selected_tools]
            
#             if new_selected_tools[0]["tool_id"] == 65742:
#                 print("Ask for user input")
#             else:
#                 self.current_tool_name = tools.get_tool_name(new_selected_tools[0]["tool_id"])
#                 self.current_tool_action = new_selected_tools[0]["action"]
#                 outcome = tools.execute_action(self.current_tool_name, self.current_tool_action)
#                 self.prev_outcomes[self.current_tool_action] = outcome
#                 review = Review(self.review_data, info_required, self.current_task_details["current_task"])
#                 print(self.current_task_details["current_task"])
#                 print(info_required)
#                 findings = review.review_info()
#                 if not findings["have_all_required_inputs"]:
#                     print("First Ask User Funciton")
#                     self.tasks_pipeline.pop(0)
#                     init_execution = TaskExecutor(self.user_input, self.tasks_pipeline, self.current_task_details, self.selected_tools)
#                     init_execution.executor()
#                 else:
#                     self.tasks_pipeline.pop(0)
#                     init_execution = TaskExecutor(self.user_input, self.tasks_pipeline, self.current_task_details, self.selected_tools)
#                     init_execution.executor()
#             return False
                

#         print("Proceed with execution of the action")
#         key_value_pair = {key: value for key, value in findings.items() if key not in ['current_task_id', 'have_all_required_inputs']}
#         input_params = {}
#         for key, value_from_findings in key_value_pair.items():
#             value_from_prev_outcomes = self.prev_outcomes.get(value_from_findings)
#             if value_from_prev_outcomes is not None:
#                 if value_from_findings == "user_input":
#                     input_params[key] = "value from openai api call"
#                 else:  
#                     input_params[key] = value_from_prev_outcomes

#             outcome = tools.execute_action(self.current_tool_name, self.current_tool_action, **input_params)
#             # print("Outcome")
#             # print(outcome)
#             self.prev_outcomes[self.current_tool_action] = outcome
#             self.tasks_pipeline.pop(0)

#         return False


from tools_store import Tools
from thinkslow.review import Review
from thinkslow.select_tools import SelectTools
from utils.utilities import Utilities


class TaskExecutor:
    def __init__(self, user_input, tasks_pipeline, current_task_details, selected_tools, chat):
        self.chat = chat
        self.user_input = user_input
        self.tasks_pipeline = tasks_pipeline
        self.selected_tools = selected_tools
        self.current_task_details = current_task_details
        self.prev_outcomes = {}
        self.review_data = []
        self.tools = Tools()

    def execute_task(self, tool_name, tool_action, input_params=None):
        outcome = self.tools.execute_action(tool_name, tool_action, **(input_params or {}))
        self.prev_outcomes[tool_action] = outcome
        self.tasks_pipeline.pop(0)

    def executor(self):
        if not self.tasks_pipeline:
            return True

        self.current_task_details = Utilities.get_current_task_details(self.tasks_pipeline, self.selected_tools)
        if self.current_task_details is None:
            raise Exception("Error: No current task details found")

        if self.current_task_details["action"] == "final_response":
            print("Final response")
            return True

        self.current_tool_id = self.current_task_details["tool_id"]
        self.current_tool_name = self.tools.get_tool_name(self.current_tool_id)
        self.current_tool_action = self.current_task_details["action"]

        info_required = self.tools.get_info_required(self.current_tool_name, self.current_tool_action)
        print("Info required")
        print(info_required)

        if info_required is None:
            self.execute_task(self.current_tool_name, self.current_tool_action)
            return self.executor()
        else:
            self.review_data.append({
                "user_input": self.user_input,
                "prev_outcomes": self.prev_outcomes
            })

            review = Review(self.review_data, info_required, self.current_task_details["current_task"], self.chat)
            findings = review.review_info()

            if findings["have_all_required_inputs"]:
                key_value_pair = {key: value for key, value in findings.items() if key not in ['current_task_id', 'have_all_required_inputs']}
                input_params = {}
                for key, value_from_findings in key_value_pair.items():
                    value_from_prev_outcomes = self.prev_outcomes.get(value_from_findings)
                    if value_from_prev_outcomes is not None:
                        input_params[key] = "value from openai api call" if value_from_findings == "user_input" else value_from_prev_outcomes
                
                self.execute_task(self.current_tool_name, self.current_tool_action, input_params)
                return self.executor()
            else:
                new_task_id = len(self.tasks_pipeline)
                self.tasks_pipeline.insert(0, {"task_id": new_task_id, "task": findings["new_task"]})
                find_tools = SelectTools(self.user_input, self.tasks_pipeline[0], True, self.chat)
                new_selected_tools = find_tools.select_tools()
                # Ensure selected_tools is a list
                if isinstance(new_selected_tools, dict):
                    new_selected_tools = [new_selected_tools]
                if new_selected_tools[0]["tool_id"] == 65742:
                    print("Ask for user input")
                    self.tasks_pipeline.pop(0)
                    return self.executor()
                else:
                    self.current_tool_name = self.tools.get_tool_name(new_selected_tools[0]["tool_id"])
                    self.current_tool_action = new_selected_tools[0]["action"]
                    self.execute_task(self.current_tool_name, self.current_tool_action)
                    review = Review(self.review_data, info_required, self.current_task_details["current_task"], self.chat)
                    findings = review.review_info()
                    if not findings["have_all_required_inputs"]:
                        print("First Ask User Function")
                        self.tasks_pipeline.pop(0)
                        return self.executor()
                    else:
                        self.tasks_pipeline.pop(0)
                        return self.executor()
