class StringManipulation:
    def __init__(self, words):
        self.words = words

    def total_words(self):
        return len(self.words)

    def count(self, some_word):
        count = 0
        for word in self.words:
            if (word == some_word):
                count += 1
        return count

    def words_of_length(self, length):
        l = []
        for word in self.words:
            if (len(word) == length):
                l.append(word)
        return l

    def words_start_with(self, char):
        l = []
        for word in self.words:
            if (word.startswith(char)):
                l.append(word)
        return l

    def longest_word(self):
        long_word = max(self.words, key = len)
        return long_word

    def palindromes(self):
        l = []
        for word in self.words:
            p = ''
            for i in word:
                p = i + p
            if (word == p):
                l.append(word)
        return l


L = StringManipulation(['vishwa', 'kunj', 'sonal', 'vishwa', 'sandip', '22022', 'malayalam'])
print(L.total_words())
print(L.count('vishwa'))
print(L.words_of_length(6))
print(L.words_start_with('s'))
print(L.longest_word())
print(L.palindromes())