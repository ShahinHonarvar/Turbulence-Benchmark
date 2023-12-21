
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}
    for word in my_list:
        # Convert the word to lowercase and sort it alphabetically
        sorted_word = "".join(sorted(word.lower()))
        # If the sorted word is already in the dictionary, increase its count by 1
        if sorted_word in anagram_pairs:
            anagram_pairs[sorted_word] += 1
        # Otherwise, add it to the dictionary with a count of 1
        else:
            anagram_pairs[sorted_word] = 1
    # Return True if there are at least 47 pairs of anagrams in the list
    return len(anagram_pairs) >= 47
