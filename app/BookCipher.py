from app.Key import Key


class BookCipher:
    @staticmethod
    def encode(text: str, key: Key):
        code = []
        for ch in text:
            if ch.isalpha():
                ch_code = str(key.index(ch))
                if ch.isupper():
                    ch_code = f'U{ch_code}'
                code.append(ch_code)
            elif ch.isnumeric():
                code.append(f'!{ch}')
            elif ch == '&':
                code.append('and')
            elif ch == '!':
                code.append('!!')
            else:
                code.append(ch)

        return '&'.join(code)

    @staticmethod
    def decode(text: str, key: Key):
        decoded_text = ''
        for item in text.split('&'):
            if item.isnumeric():
                decoded_text += key.char_at(int(item))
            elif item[0] == 'U':
                decoded_text += key.char_at(int(item[1:])).upper()
            elif item[0] == '!':
                decoded_text += item[1]
            elif item == 'and':
                decoded_text += '&'
            else:
                decoded_text += item

        return decoded_text
