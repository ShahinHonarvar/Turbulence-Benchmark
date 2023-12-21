
def if_contains_anagrams(str_list):
    # Create a set of all possible anagrams of the English letters
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    all_anagrams = []
    for i in range(26):
        for j in range(i+1, 26):
            anagram = english_letters[i] + english_letters[j]
            all_anagrams.append(anagram)
    # Create a set of all possible pairs of anagrams
    all_pairs = []
    for i in range(len(all_anagrams)):
        for j in range(i+1, len(all_anagrams)):
            pair = (all_anagrams[i], all_anagrams[j])
            all_pairs.append(pair)
    # Check if there are at most 92 pairs of anagrams in the given list
    num_pairs = 0
    for str1, str2 in all_pairs:
        if str1 in str_list and str2 in str_list:
            num_pairs += 1
    return num_pairs <= 92
