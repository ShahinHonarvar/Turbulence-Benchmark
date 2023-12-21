
def if_contains_anagrams(strings):
    def count_anagrams(string):
        count = 0
        for i in range(len(strings)):
            if sorted(string.lower()) == sorted(strings[i].lower()):
                count += 1
        return count

    anagram_pairs = 0
    for string in strings:
        if count_anagrams(string) >= 2:
            anagram_pairs += count_anagrams(string) - 1

    return anagram_pairs >= 155
