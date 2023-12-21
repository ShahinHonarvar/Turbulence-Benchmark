
def if_contains_anagrams(words):
    word_count = {}
    for word in words:
        if len(word) < 3:
            continue

        anagram = "".join(sorted(word))

        if anagram in word_count:
            word_count[anagram] += 1

        else:
            word_count[anagram] = 1

    for key, value in word_count.items():
        if value >= 46:
            return True

    return False
