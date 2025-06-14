
def if_contains_anagrams(my_list):
    # Define the English alphabet and its corresponding anagram
    english_alphabet = "abcdefghijklmnopqrstuvwxyz"
    english_alphabet_anagram = list(english_alphabet)
    # Initialize variables to keep track of anagrams
    num_anagrams = 0
    num_pairs = 0
    # Iterate through the list of strings and check for anagrams
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list))):
            # Check if the current string is an anagram of the previous string
            if sorted(my_list[j].lower()) == sorted(my_list[i].lower()):
                # Increment the number of anagrams and pairs found
                num_anagrams += 1
                num_pairs += 1
    # Return True if there are at most 59 pairs of anagrams in the list, otherwise return False
    if num_pairs <= 59:
        return True
    else:
        return False
