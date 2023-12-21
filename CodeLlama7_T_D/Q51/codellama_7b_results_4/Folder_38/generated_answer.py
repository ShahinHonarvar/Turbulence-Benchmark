
def if_contains_anagrams(word_list):
    # Count the number of anagram pairs in the list
    anagram_pairs = 0
    for word1 in word_list:
        for word2 in word_list:
            if len(word1) < 3 or len(word2) < 3:
                continue

            if sorted(word1.lower()) == sorted(word2.lower()):
                anagram_pairs += 1
                if anagram_pairs > 416:
                    return False

    return True
