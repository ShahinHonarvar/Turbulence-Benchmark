
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        string = string.lower()

        # Check if the string is at least three characters long
        if len(string) >= 3:
            # Sort the characters of the string
            sorted_string = "".join(sorted(string))

            # Check if the sorted string is in the anagram pairs dictionary
            if sorted_string in anagram_pairs:
                # Increment the count for the sorted string
                anagram_pairs[sorted_string] += 1

            # If the sorted string is not in the anagram pairs dictionary, add it with a count of 1
            else:
                anagram_pairs[sorted_string] = 1

    # Check if there are at least 24 pairs of anagrams in the list
    if len(anagram_pairs) >= 24:
        return True

    # If there are not enough anagram pairs, return False
    else:
        return False
