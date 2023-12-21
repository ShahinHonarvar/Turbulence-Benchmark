
def if_contains_anagrams(strings):
    # check if there are at least 49 pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                num_pairs += 1
                if num_pairs >= 49:
                    return True

    # check if there are at least three anagrams in the list
    anagram_count = {}

    for string in strings:
        anagram = ''.join(sorted(string))

        if anagram in anagram_count:
            anagram_count[anagram] += 1

        else:
            anagram_count[anagram] = 1

    for key, value in anagram_count.items():
        if value >= 3:
            return True

    # no anagrams found
    return False
