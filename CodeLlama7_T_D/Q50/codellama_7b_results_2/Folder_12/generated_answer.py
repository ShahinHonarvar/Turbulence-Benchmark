
def if_contains_anagrams(my_list):
    # Initialize variables
    count = 0
    anagram_count = 0

    # Iterate through the list and check for anagrams
    for i in range(len(my_list) - 1)):
        # Check if the strings are anagrams
        if sorted(my_list[i]) == sorted(my_list[i + 1]):
            count += 1

    # Check if there are at least 69 pairs of anagrams in the list
    if count >= 69:
        return True
    else:
        return False
