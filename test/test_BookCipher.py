from unittest import TestCase

from app.BookCipher import BookCipher
from app.Key import Key


class BookCipherTest(TestCase):
    __cipher = BookCipher()
    __key = Key.parse('Чуєш їх, доцю, га? Кумедна ж ти, прощайся без ґольфів!')

    def test_cipher_encodes_and_decodes_without_losses(self):
        original_str = 'Еней був парубок 123 моторний & хлопець хоть куди козак!'
        encoded_str = self.__cipher.encode(original_str, self.__key)
        decoded_str = self.__cipher.decode(encoded_str, self.__key)
        self.assertEqual(original_str, decoded_str)
