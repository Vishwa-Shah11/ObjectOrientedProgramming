class StringManipulation:
    def __init__(self, words):
        self.words = words

    def total_words(self):
        return len(self.words)

    def count(self, some_word):
        count = 0
        for word in self.words:
            if (word == self.some_word):
                count += 1
        return count


L = StringManipulation(['Vishwa', 'Kunj', 'Sonal', 'Sandip'])
print(L.total_words())
print(L.count('Vishwa'))