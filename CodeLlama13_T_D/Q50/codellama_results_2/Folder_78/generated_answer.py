
def if_contains_anagrams(strings):
    anagram_pairs = []
    for string in strings:
        lowercase_string = string.lower()
        for i in range(len(lowercase_string) - 2):
            substr = lowercase_string[i:i+3]
            if substr not in anagram_pairs:
                anagram_pairs.append(substr)
    return len(anagram_pairs) >= 79
