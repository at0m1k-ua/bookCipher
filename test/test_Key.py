from unittest import TestCase

from app.Key import Key


class KeyTest(TestCase):
    def test_key_parse_works_for_ukrainian(self):
        key = Key.parse('Еней був парубок моторний')
        self.assertEqual('енейбувпарубокмоторний', key._phrase)

    def test_key_parse_works_for_latin(self):
        key = Key.parse('To be or not to be 12341234')
        self.assertEqual('tobeornottobe', key._phrase)

    def test_key_returns_first_index(self):
        key = Key.parse('Мені тринадцятий минало')
        self.assertEqual(2, key.index('н'))

    def test_key_raises_exception_with_empty_char_string(self):
        key = Key.parse('hello world')
        with self.assertRaises(ValueError):
            key.index('')

    def test_key_raises_exception_with_too_big_char_string(self):
        key = Key.parse('hello world')
        with self.assertRaises(ValueError):
            key.index('el')
