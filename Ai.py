from asyncio import run_coroutine_threadsafe
import os
from typing import List
import openai

class Ai:

    def __init__(self, key_words: str, word_count: int, is_list: bool):
        self.key_words = key_words
        self.word_count = word_count
        self.is_list = is_list
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def words_to_token(self, words):
        return round(words*1.333)

    def get_text(self):
        search = f"Erstelle einen SEO text mit dem folgenden Keywords: {self.key_words}. Er muss einen Einleitungssatz {'und Aufzählungen' if self.is_list else ''} enthalten. SEO text: "
        response = openai.Completion.create(
                model="text-davinci-003",
                prompt=search,
                temperature=0,
                max_tokens= self.words_to_token(self.word_count),
                top_p=1,
                frequency_penalty=0.5,
                presence_penalty=0
            )
        print(response)
        return response.choices[0].text
        

