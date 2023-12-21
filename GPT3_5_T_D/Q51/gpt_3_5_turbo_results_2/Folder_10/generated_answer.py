
def if_contains_anagrams(string_list):
    def count_chars(string):
        char_counts = {}
        for char in string.lower():
            if char.isalpha():
                if char in char_counts:
                    char_counts[char] += 1
                else:
                    char_counts[char] = 1
        return char_counts

    def is_anagram(string1, string2):
        return count_chars(string1) == count_chars(string2)

    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
                if is_anagram(string_list[i], string_list[j]):
                    anagram_count += 1
                    if anagram_count > 21:
                        return False
    return True
