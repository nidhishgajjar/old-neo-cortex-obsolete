from spock.memory import Memory
from spock.mind import mind

def main():
    memory = Memory()
    while True:
        user_input = input("User: ")
        context = memory.get_chat_history() 
        chad = mind(user_input, context)
        chad_response = chad.system1()
        memory.short_term(user_input, chad_response)
        chad.system2()

if __name__ == "__main__":
    main()
 