
def if_contains_anagrams(words):
    # check if there are at least 7 pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                num_pairs += 1
                if num_pairs >= 7:
                    return True

    # check if there are at least three anagrams of the same length in the list
    lengths = set()

    for word in words:
        lengths.add(len(word))

    if len(lengths) < 3:
        return False

    # compare the strings in a case-insensitive manner
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if sorted(words[i].lower()) == sorted(words[j].lower()):
                return True

    return False
