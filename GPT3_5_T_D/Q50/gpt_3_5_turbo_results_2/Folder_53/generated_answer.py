
def if_contains_anagrams(strings):

    def is_anagram(word1, word2):
        letters1 = [letter.lower() for letter in word1 if letter.isalpha()]
        letters2 = [letter.lower() for letter in word2 if letter.isalpha()]
        return sorted(letters1) == sorted(letters2) and len(letters1) >= 3

    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count == 11:
                    return True
    return False
