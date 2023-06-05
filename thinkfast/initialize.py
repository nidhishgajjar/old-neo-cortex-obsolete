
from ai import OpenAIChat
from thinkfast.instinct import Instinct
from thinkfast.introspect import Introspect


class ThinkFast:
    def __init__(self, user_input, context):
        self.chat = OpenAIChat()
        self.user_input = user_input
        self.context = context
        self.instinct = Instinct(self.user_input, self.context, self.chat)
        self.introspect = Introspect(self.chat)
        self.response = None

    def run(self):
        self.response = self.instinct.trigger()
        return self.response
    
    def introspection(self): 
        return self.introspect.trigger(self.user_input, self.response)