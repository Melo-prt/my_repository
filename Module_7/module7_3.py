class WordsFinder:
    def __init__(self, *name):
        self.file_names = name

    def get_all_words(self):
        all_words = {}
        symbols_to_delete = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                list_words =[]
                for line in file:
                    line = line.lower()
                    for symbol in symbols_to_delete:
                        if line.count(symbol):
                            line = line.replace(symbol, '')
                    line = line.split()
                    list_words.append(line)
                new_list = []
                for word in list_words:
                    new_list += word
                all_words[name] = new_list
        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            word = word.lower()
            number_of_word = 0
            for i in words:
                number_of_word += 1
                if word == i:
                    print(f'{name}: {number_of_word}')

    def count(self, word):
        for name, words in self.get_all_words().items():
            word = word.lower()
            count_of_word = 0
            for i in words:
                if word == i:
                    count_of_word += 1
            if count_of_word != 0:
                print(f'{name}: {count_of_word}')

finder2 = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

