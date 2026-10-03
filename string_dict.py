from string_hash import string_hash


class StringDictionary:
    def __init__(self, size=16):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.count = 0

    def _index(self, key):
        return string_hash(key) % self.size

    def add(self, key):
        index = self._index(key)
        bucket = self.table[index]

        for k, _ in bucket:
            if k == key:
                return  # уже есть

        bucket.append((key, string_hash(key)))
        self.count += 1

    def get(self, key):
        index = self._index(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"  [{i}] {bucket}")