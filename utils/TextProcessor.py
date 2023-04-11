import re
from string import punctuation

from nltk.corpus import stopwords
from pymystem3 import Mystem


class TextProcessor:
    def __init__(self) -> None:
        self.mystem = Mystem()
        self.stopwords = stopwords.words("russian")

    def remove_punctuation(self, text: str):
        chars_no_punctuation = [char if char not in punctuation + '«»' else ' ' for char in text ]
        return ''.join(chars_no_punctuation)

    def lemmatize(self, text: str):
        tokens = self.mystem.lemmatize(text.lower())
        return tokens

    def remove_trash(self, tokens: list):
        def remove_stop_words(tokens: list):
            return [ token for token in tokens
                    if token not in self.stopwords and
                    token != ' ' and
                    token.strip() not in punctuation ]

        def remove_digits(tokens: list):
            return [token for token in tokens if token not in '0123456789']

        def remove_short_tokens(tokens: list):
            return [token for token in tokens if len(token) >= 3]

        tokens = remove_stop_words(tokens)
        tokens = remove_digits(tokens)
        tokens = remove_short_tokens(tokens)
        return tokens

    def remove_emojis(self, text: str):
        emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            "]+", flags=re.UNICODE)
        text = emoji_pattern.sub(r'', text)
        return text

    def process(self, text: str):
        text = self.remove_punctuation(text)
        tokens = self.lemmatize(text)
        tokens = self.remove_trash(tokens)
        text = ' '.join(tokens).replace('\n', ' ')
        text = self.remove_emojis(text)
        return text
    
