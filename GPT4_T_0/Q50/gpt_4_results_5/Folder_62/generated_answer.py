
def if_contains_anagrams(lst):
    from collections import defaultdict

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)

    count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2

    return count >= 43
