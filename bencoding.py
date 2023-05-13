from collections import OrderedDict


TOKEN_INT = b'i'
TOKEN_LIST = b'l'
TOKEN_DICT = b'd'
TOKEN_END = b'e'
TOKEN_SEPARATOR_STRING = b':'


class Decoder:
    def __init__(self, b: bytes) -> None:
        self.b = b
        self._index = 0

    def _peek(self):
        return self.b[self._index:self._index + 1]

    def decode(self):
        char = self._peek()
        if char == TOKEN_INT:
            self._index += 1
            return self._decode_integer()
        if char in b'0123456789':
            return self._decode_string()
        if char == TOKEN_LIST:
            self._index += 1
            return self._decode_list()
        if char == TOKEN_DICT:
            self._index += 1
            return self._decode_dictionary()

    def _decode_integer(self):
        counter = self._index
        for char in self.b[self._index:]:
            counter += 1
            if b'%c' % char == TOKEN_END:
                break
        num = int(self.b[self._index:counter - 1])
        self._index = counter
        return num

    def _decode_string(self):
        counter = self._index
        for char in self.b[self._index:]:
            counter += 1
            if b'%c' % char == TOKEN_SEPARATOR_STRING:
                break
        num = int(self.b[self._index:counter - 1])
        string = self.b[counter:counter + num]
        self._index = counter + num
        return string

    def _decode_list(self):
        res = []
        while self.b[self._index: self._index + 1] != TOKEN_END:
            res.append(self.decode())
        self._index += 1
        return res

    def _decode_dictionary(self):
        res = OrderedDict()
        while self.b[self._index: self._index + 1] != TOKEN_END:
            key = self.decode()
            obj = self.decode()
            res[key] = obj
        self._index += 1
        return res
