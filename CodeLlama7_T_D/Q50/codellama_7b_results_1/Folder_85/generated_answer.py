
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                anagram_pairs += 1
                if anagram_pairs >= 73:
                    return True

    return False
