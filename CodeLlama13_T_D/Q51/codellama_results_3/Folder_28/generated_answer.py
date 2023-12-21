
def if_contains_anagrams(words):
    anagram_pairs = 0
    for word1 in words:
        for word2 in words:
            if len(word1) >= 3 and len(word2) >= 3:
                if word1.lower() == word2.lower():
                    continue
                if "".join(sorted(list(word1))) == "".join(sorted(list(word2))):
                    anagram_pairs += 1
            if anagram_pairs > 78:
                return False
    return True
