from conversation import Conversation

def main():
    user_input = "How are you? "
    conversation = Conversation(user_input)
    conversation.task_request()

if __name__ == "__main__":
    main()