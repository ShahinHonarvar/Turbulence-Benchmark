
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagram pairs
    pair_count = 0
    three_or_more_letter_count = 0
    # Iterate over the list of strings
    for string in my_list:
        # Get a list of all possible anagrams of the current string
        possible_anagrams = []
        for i in range(len(string) - 1):
            for j in range(i + 1, len(string)):
                possible_anagrams.append((string[i] + string[j]), (string[j] + string[i]))
        # Increment the pair count for each anagram pair found
        for anagram_pair in possible_anagrams:
            if (len(anagram_pair[0]) > 2) and (len(anagram_pair[1]) > 2):
                pair_count += 1
                three_or_more_letter_count += len(anagram_pair[0]) + len(anagram_pair[1])
    # Return true if there are at least 65 pairs of anagrams in the given list, otherwise return false
    return (pair_count >= 65) and (three_or_more_letter_count > 380)
