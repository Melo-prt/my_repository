
def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)
    return same_words


root_word = 'rich'
other_words = 'rich', 'richiest', 'orichalcum', 'cheers', 'richies'
print(f"Слова с корнем '{root_word}': {single_root_words(root_word, *other_words)}")


root_word = 'Able'
other_words = 'Disablement', 'Able', 'Mable', 'Disable', 'Bagel'
print(f"Слова с корнем '{root_word}': {single_root_words(root_word, *other_words)}")