import json

class Summarizer:

    @staticmethod
    def create_summary_info_required():
        return json.dumps({"text": "text to summarize"})

    @staticmethod
    def create_summary(*args, **kwargs):
        text = kwargs.get('text')
        print(f"Summarizing text: {text}")