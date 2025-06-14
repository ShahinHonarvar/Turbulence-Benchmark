
def if_contains_anagrams(word_list):
    # Check if there are at least 75 pairs of anagrams in the given list
    num_pairs = 0
    for i in range(len(word_list) - 1)):
        for j in range(i + 1, len(word_list))):
            # Check if the words are anagrams by comparing their sorted forms
            if sorted(word_list[i]) == sorted(word_list[j])):
                num_pairs += 1
    return num_pairs >= 75
