
def if_contains_anagrams(list):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = 0
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if len(list[i]) >= 3 and len(list[j]) >= 3 and is_anagram(list[i], list[j]):
                anagram_pairs += 1
    return anagram_pairs <= 17
