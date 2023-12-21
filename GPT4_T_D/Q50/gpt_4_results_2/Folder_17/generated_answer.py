
def if_contains_anagrams(string_list):
    from collections import defaultdict

    def sorted_string(s):
        return ''.join(sorted(s.lower()))

    sorted_strings = defaultdict(int)
    for string in string_list:
        if len(string) >= 3:
            sorted_strings[sorted_string(string)] += 1

    anagram_pairs = sum(count * (count - 1) // 2 for count in sorted_strings.values())

    return anagram_pairs >= 97
