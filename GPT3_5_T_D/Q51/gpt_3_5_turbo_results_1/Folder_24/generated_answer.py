
def if_contains_anagrams(lst):
    def count_chars(string):
        char_count = [0] * 26
        for char in string.lower():
            if char.isalpha():
                char_count[ord(char) - ord('a')] += 1
        return tuple(char_count)

    char_count_dict = {}
    for string in lst:
        if len(string) >= 3:
            char_count = count_chars(string)
            char_count_dict[char_count] = char_count_dict.get(char_count, 0) + 1

    anagram_pairs = sum(count * (count - 1) // 2 for count in char_count_dict.values())
    return anagram_pairs <= 96
