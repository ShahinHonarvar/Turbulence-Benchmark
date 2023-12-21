
def if_contains_anagrams(strings):
    def count_chars(string):
        char_count = [0] * 26
        for char in string:
            if char.isalpha():
                char_count[ord(char.lower()) - ord('a')] += 1
        return tuple(char_count)

    anagram_count = {}
    for string in strings:
        if len(string) >= 3 and string.isalpha():
            char_count = count_chars(string)
            if char_count in anagram_count:
                anagram_count[char_count] += 1
            else:
                anagram_count[char_count] = 1

    total_anagrams = sum(anagram_count.values())
    return total_anagrams <= 52
