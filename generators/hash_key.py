
import hashlib
import uuid


def key(keyword, how_many):
    count = []
    while how_many > 0:

        salt = uuid.uuid4().hex
        hash_key = hashlib.sha224(salt.encode() + keyword.encode()).hexdigest()
        to_str = str(hash_key)
        cut_str = to_str
        if cut_str not in count:
            count.append(cut_str)
            how_many -= 1
        return cut_str
