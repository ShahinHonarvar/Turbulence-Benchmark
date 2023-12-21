
def if_contains_anagrams(input_list):
    def is_anagram(word1, word2):
        if len(word1) != len(word2):
            return False
        return sorted(word1.lower()) == sorted(word2.lower())

    count = 0
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            if is_anagram(input_list[i], input_list[j]):
                count += 1

    return count >= 92
