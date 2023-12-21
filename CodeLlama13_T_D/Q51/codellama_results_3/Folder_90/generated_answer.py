
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for string1 in strings:
        for string2 in strings:
            if len(string1) >= 3 and len(string2) >= 3 and string1.lower() != string2.lower():
                if sorted(string1) == sorted(string2):
                    anagram_pairs += 1
    return anagram_pairs <= 147
