
def if_contains_anagrams(string_list):
    anagram_pairs = set()
    for s in string_list:
        for i in range(len(s) - 2):
            substring = s[i : i + 3]
            if substring.lower() not in anagram_pairs:
                anagram_pairs.add(substring.lower())
    return len(anagram_pairs) <= 34
