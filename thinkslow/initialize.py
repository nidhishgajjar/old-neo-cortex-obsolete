from ai import OpenAIChat
from thinkslow.select_tools import SelectTools
from thinkslow.task_planning import TaskPlanning
from thinkslow.execution import TaskExecutor


# class ThinkSlow:
#     def __init__(self, user_input):
#         self.user_input = user_input
#         self.tasks_pipeline = None
#         self.selected_tools = None
#         self.current_task_details = None
#         self.current_tool_id = None
#         self.current_tool_name = None
#         self.current_tool_action = None

#     def run(self):

#         task_planning = TaskPlanning(self.user_input)
#         self.tasks_pipeline = task_planning.tasks()
#         # print(self.tasks_pipeline)

#         if self.tasks_pipeline:
#             find_tools = SelectTools(self.user_input, self.tasks_pipeline, False)
#             self.selected_tools = find_tools.select_tools()
#             # print(self.selected_tools)
                    
#             init_execution = TaskExecutor(self.user_input, self.tasks_pipeline, self.current_task_details, self.selected_tools)
#             while init_execution.executor() is not True:
#                 pass



class ThinkSlow:
    def __init__(self, user_input):
        self.chat = OpenAIChat()
        self.user_input = user_input
        self._tasks_pipeline = None
        self._selected_tools = None
        self._current_task_details = None

    def set_tasks_pipeline(self, tasks):
        self._tasks_pipeline = tasks

    def set_selected_tools(self, tools):
        self._selected_tools = tools

    def set_current_task_details(self, details):
        self._current_task_details = details

    def run(self):
        task_planning = TaskPlanning(self.user_input, self.chat)
        self.set_tasks_pipeline(task_planning.tasks())
        
        if self._tasks_pipeline:
            find_tools = SelectTools(self.user_input, self._tasks_pipeline, False, self.chat)
            self.set_selected_tools(find_tools.select_tools())

            init_execution = TaskExecutor(self.user_input, self._tasks_pipeline, self._current_task_details, self._selected_tools, self.chat)
            while not init_execution.executor():
                pass
