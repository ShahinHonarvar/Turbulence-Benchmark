
def if_contains_anagrams(strings):
    def count_letters(word):
        count = [0] * 26
        for char in word:
            if char.isalpha():
                count[ord(char.lower()) - ord('a')] += 1
        return tuple(count)

    anagram_pairs = 0
    letter_count = dict()
    for word in strings:
        if len(word) >= 3:
            count = count_letters(word)
            if count in letter_count:
                letter_count[count] += 1
                if letter_count[count] == 2:
                    anagram_pairs += 1
            else:
                letter_count[count] = 1
    
    return anagram_pairs <= 401
