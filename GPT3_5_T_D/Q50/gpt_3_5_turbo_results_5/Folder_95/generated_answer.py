
def if_contains_anagrams(input_list):
    def is_anagram(word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        return sorted(word1) == sorted(word2) and len(word1) >= 3

    count = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if is_anagram(input_list[i], input_list[j]):
                count += 1
                if count >= 93:
                    return True
    return False
