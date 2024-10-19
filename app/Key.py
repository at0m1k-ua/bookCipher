class Key:
    def __init__(self, phrase: str):
        self._phrase = phrase

    def index(self, ch):
        ch_len = len(ch)
        if ch_len != 1:
            raise ValueError('Length of character string should be 1, '
                             f'actual = {ch_len}')

        return self._phrase.index(ch.lower())

    @staticmethod
    def parse(input_phrase: str):
        final_phrase = ''
        for ch in input_phrase:
            if ch.isalpha():
                final_phrase += ch.lower()

        return Key(final_phrase)

    def char_at(self, i):
        return self._phrase[i]
