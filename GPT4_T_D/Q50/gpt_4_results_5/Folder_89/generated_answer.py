
def if_contains_anagrams(words):
    word_dict = {}
    count = 0
    for word in words:
        key = "".join(sorted(word.lower()))
        if word_dict.get(key):
            word_dict[key].append(word)
        else:
            word_dict[key] = [word]

    for value in word_dict.values():
        if len(value) > 1 and len(value[0])>=3:
            count += len(value) * (len(value) - 1) // 2
        if count >= 36:
            return True

    return False
