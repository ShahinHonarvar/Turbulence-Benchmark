
def if_contains_anagrams(word_list):
    word_list = [word.lower() for word in word_list if len(word) >= 3]
    anagram_count = 0
    for i in range(len(word_list)):
        for j in range(i+1, len(word_list)):
            if sorted(word_list[i]) == sorted(word_list[j]):
                anagram_count += 1
                if anagram_count > 74:
                    return False
    return True
