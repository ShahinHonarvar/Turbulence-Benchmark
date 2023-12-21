
def if_contains_anagrams(str_list):
    def count_letters(string):
        letter_count = {}
        for letter in string:
            if letter.isalpha():
                if letter.lower() in letter_count:
                    letter_count[letter.lower()] += 1
                else:
                    letter_count[letter.lower()] = 1
        return tuple(sorted(letter_count.items()))

    anagram_count = {}
    for string in str_list:
        if len(string) >= 3:
            letters = count_letters(string)
            if letters in anagram_count:
                anagram_count[letters] += 1
            else:
                anagram_count[letters] = 1

    total_anagrams = 0
    for count in anagram_count.values():
        total_anagrams += count * (count - 1) // 2

    return total_anagrams >= 188
