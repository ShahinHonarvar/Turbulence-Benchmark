
def if_contains_anagrams(list_of_strings):
    def count_anagrams(string):
        is_anagram = lambda a, b: sorted(a.lower()) == sorted(b.lower())
        anagram_count = 0
        for i in range(len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and is_anagram(string, list_of_strings[i]):
                anagram_count += 1
        return anagram_count

    pair_count = 0
    for i in range(len(list_of_strings)):
        if count_anagrams(list_of_strings[i]) >= 2:
            pair_count += 1
            if pair_count > 17:
                return False
    return True
