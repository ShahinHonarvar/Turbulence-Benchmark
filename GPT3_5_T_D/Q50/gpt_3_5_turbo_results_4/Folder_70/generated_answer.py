
def if_contains_anagrams(string_list):
    def count_chars(s):
        char_count = [0] * 26
        for char in s:
            if char.isalpha():
                char_count[ord(char.lower()) - 97] += 1
        return tuple(char_count)

    anagram_pairs = 0
    word_counts = {}

    for word in string_list:
        if len(word) >= 3:
            word_count = count_chars(word)
            if word_count in word_counts:
                anagram_pairs += word_counts[word_count]
                word_counts[word_count] += 1
            else:
                word_counts[word_count] = 1

    return anagram_pairs >= 189
