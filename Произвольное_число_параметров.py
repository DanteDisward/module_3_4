def single_root_words(root_word, *other_words):
    same_words = []
    other_words_list = [*other_words]
    root_word_low = root_word.lower()
    for item in other_words_list:
        x = str(item).lower()
        if root_word_low in x or x in root_word_low:
            same_words.append(item)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
