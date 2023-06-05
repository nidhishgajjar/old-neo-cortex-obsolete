import tiktoken

class Memory:
    def __init__(self):
        self.chat_history = []
        self.token_limit = 2700
        self.encoding = tiktoken.get_encoding("cl100k_base")

    def token_count(self, text):
        return len(self.encoding.encode(text)) + 4  # accounted for message overhead
    
    def get_chat_history(self):
        chat_history_without_tokens = [{'User': pair['User'], 'Chad': pair['Chad']} for pair in self.chat_history]
        return chat_history_without_tokens


    def short_term(self, user_input, chad_response):
        new_pair = {'User': user_input, 'Chad': chad_response}
        new_pair_token_count = self.token_count(new_pair['User']) + self.token_count(new_pair['Chad'])
        new_pair['tokens'] = new_pair_token_count
        total_token_count = sum(pair['tokens'] for pair in self.chat_history)

        while total_token_count + new_pair_token_count > self.token_limit:
            oldest_pair = self.chat_history.pop(0)
            total_token_count -= oldest_pair['tokens']

        self.chat_history.append(new_pair)

        return self.chat_history


