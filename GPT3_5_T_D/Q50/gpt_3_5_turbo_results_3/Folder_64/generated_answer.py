
def if_contains_anagrams(string_list):
    def are_anagrams(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    pairs = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3 and are_anagrams(string_list[i], string_list[j]):
                pairs += 1

    return pairs >= 5
