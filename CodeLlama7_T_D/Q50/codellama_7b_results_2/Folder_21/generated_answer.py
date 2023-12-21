
def if_contains_anagrams(my_list):
    # Count the number of anagram pairs in the list
    anagram_pairs = 0
    for i in range(len(my_list) - 1):
        # Check if the current string is a palindrome
        if my_list[i] == my_list[i][::-1]:
            # Check if there are at least three characters in the anagram
            if len(my_list[i]) >= 3:
                # Increment the number of anagram pairs
                anagram_pairs += 1
    # Return True if there are at least 136 anagram pairs in the list, False otherwise
    return anagram_pairs >= 136
