
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    for i in range(len(my_list)):
        # Get the current string and its length
        current_string = my_list[i]
        current_length = len(current_string)

        # Check if the current string is long enough to be an anagram
        if current_length < 3:
            continue

        # Create a lowercase version of the current string for comparison
        lowercase_string = current_string.lower()

        # Iterate over the remaining strings in the list
        for j in range(i + 1, len(my_list)):
            # Get the next string and its length
            next_string = my_list[j]
            next_length = len(next_string)

            # Check if the next string is long enough to be an anagram
            if next_length < 3:
                continue

            # Create a lowercase version of the next string for comparison
            lowercase_next_string = next_string.lower()

            # Check if the current string and the next string are anagrams of each other
            if sorted(lowercase_string) == sorted(lowercase_next_string):
                # Add the pair of anagrams to the dictionary
                anagram_pairs[(current_string, next_string)] = 1

    # Check if there are at least 22 pairs of anagrams in the list
    return len(anagram_pairs) >= 22
