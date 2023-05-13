from bencoding import Decoder

class Metainfo:
    def __init__(self, info, announce, announce_list, creation_date,
                 comment, created_by, encoding) -> None:
        self.info = info
        self.announce = announce
        self.announce_list= announce_list
        self.creation_date = creation_date
        self.comment = comment
        self.created_by = created_by
        self.encoding = encoding

    def __str__(self):
        return f'info: {self.info.keys()}\nannounce: {self.announce}\n' \
                f'announce_list: {self.announce_list}\n' \
                f'creation_date: {self.creation_date}\n' \
                f'comment: {self.comment}\ncreated_by: {self.created_by}\n' \
                f'encoding: {self.encoding}\n'

    @staticmethod
    def from_file(path: str):
        with open(path, 'rb') as f:
            bytedata = f.read()
        d = Decoder(bytedata).decode()
        print(d.keys())
        return Metainfo.from_dict(d)

    @staticmethod
    def from_dict(dict: dict):
        return Metainfo(dict[b"info"], dict[b"announce"],
                        dict[b"announce-list"], dict[b"creation date"],
                        dict[b"comment"], dict[b"created by"],
                        dict[b"encoding"])
