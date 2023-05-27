from tools_store import Tools
from thinkflow.select_tools import SelectTools
from thinkflow.task_planning import TaskPlanning
from utils.utilities import Utilities


class Flow:
    def __init__(self, user_input):
        self.user_input = user_input
        self.tasks_pipeline = None
        self.selected_tools = None
        self.current_task_details = None
        self.current_tool_id = None
        self.current_tool_name = None
        self.current_tool_action = None

    def run(self):
        tools = Tools()

        task_planning = TaskPlanning(self.user_input)
        self.tasks_pipeline = task_planning.tasks()
        print(self.tasks_pipeline)

        if self.tasks_pipeline:
            find_tools = SelectTools(self.user_input, self.tasks_pipeline)
            self.selected_tools = find_tools.select_tools()
            print(self.selected_tools)

            self.current_task_details = Utilities.get_current_task_details(self.tasks_pipeline, self.selected_tools)
            if self.current_task_details is not None:
                self.current_tool_id = self.current_task_details["tool_id"]
                self.current_tool_name = tools.get_tool_name(self.current_tool_id)
                self.current_tool_action = self.current_task_details["action"]
                print(self.current_tool_name)
                print(self.current_tool_action)
            else:
                print("Error: No current task details found")