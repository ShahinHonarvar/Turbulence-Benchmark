
def if_contains_anagrams(string_list):
    from collections import defaultdict

    def get_anagram_key(word):
        return str(sorted(word.lower()))

    anagram_dict = defaultdict(list)
    for word in string_list:
        if len(word) >= 3:
            anagram_dict[get_anagram_key(word)].append(word)

    count = 0
    for anagram_list in anagram_dict.values():
        if len(anagram_list) > 1:
            count += len(anagram_list) // 2
            if count >= 41:
                return True  

    return count >= 41
