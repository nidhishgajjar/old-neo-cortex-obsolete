from thinkflow.flow import Flow

class Conversation:
    def __init__(self, user_input):
        self.flow = Flow(user_input)

    def task_request(self):
        self.flow.run()