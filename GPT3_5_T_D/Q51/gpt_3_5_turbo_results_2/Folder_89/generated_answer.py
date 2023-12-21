
def if_contains_anagrams(string_list):
    letter_counts = []
    anagram_count = 0

    for string in string_list:
        letters = [0] * 26
        for char in string.lower():
            if ord('a') <= ord(char) <= ord('z'):
                letters[ord(char) - ord('a')] += 1
        if letters in letter_counts:
            anagram_count += 1
        letter_counts.append(letters)

    return anagram_count <= 73
