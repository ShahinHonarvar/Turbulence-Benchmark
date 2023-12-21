
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for s in strings:
        for t in strings[strings.index(s) + 1 :]:
            if sorted(list(s)) == sorted(list(t)):
                anagram_pairs += 1
                if anagram_pairs > 65:
                    return False
    return True
