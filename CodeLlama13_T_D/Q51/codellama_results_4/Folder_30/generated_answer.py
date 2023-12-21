
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        anagram_list = []
        for c in "abcdefghijklmnopqrstuvwxyz":
            anagram_list.append(s.lower().count(c))
        anagrams.append(anagram_list)
    return sum(1 for i in range(len(anagrams)) if len(set(anagrams[i])) <= 28) == len(strings)
