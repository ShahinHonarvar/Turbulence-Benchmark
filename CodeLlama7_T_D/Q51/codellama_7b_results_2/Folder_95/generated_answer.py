
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Initialize variables for counting anagrams
    anagram_count = 0
    min_length = 3

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Check if the current string is a palindrome
        if my_list[i] == my_list[i][::-1]:
            # Increment anagram count if the length of the string is greater than or equal to three
            if len(my_list[i]) >= min_length:
                anagram_count += 1

    # Return true if there are at most six pairs of anagrams in the list, false otherwise
    return anagram_count <= 6
