
def if_contains_anagrams(word_list):
    # Count the number of pairs of anagrams in the list
    pair_count = 0
    for i in range(len(word_list) - 1):
        for j in range(i + 1, len(word_list)):
            if sorted(word_list[i]) == sorted(word_list[j]):
                pair_count += 1

    # Return True if there are at least 21 pairs of anagrams, otherwise return False
    return pair_count >= 21
