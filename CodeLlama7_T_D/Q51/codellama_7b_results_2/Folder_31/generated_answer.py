
def if_contains_anagrams(words):
    anagram_pairs = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if sorted(words[i].lower()) == sorted(words[j].lower()):
                anagram_pairs += 1
                if anagram_pairs > 65:
                    return False

    return True
