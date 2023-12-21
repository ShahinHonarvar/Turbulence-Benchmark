
def if_contains_anagrams(str_list):
    from collections import defaultdict

    def count_anagrams(str_list):
        anagram_dict = defaultdict(list)
        for word in str_list:
            if len(word) >= 3:
                key = "".join(sorted(word.lower()))
                anagram_dict[key].append(word)
        count = 0
        for words in anagram_dict.values():
            n = len(words)
            if n > 1:
                count += n*(n-1) // 2
        return count

    return count_anagrams(str_list) <= 423
