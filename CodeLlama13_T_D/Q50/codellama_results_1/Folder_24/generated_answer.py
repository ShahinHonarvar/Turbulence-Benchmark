
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for s in strings:
        for i in range(len(s) - 2):
            for j in range(i + 1, len(s)):
                if sorted(s[i:j]) == sorted(s[j:i]):
                    anagram_pairs += 1
                    break
        if anagram_pairs >= 65:
            return True
    return False
