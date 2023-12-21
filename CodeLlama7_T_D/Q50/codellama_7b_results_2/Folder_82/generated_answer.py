
def if_contains_anagrams(my_list):
    # Initialize variables
    count = 0
    anagram_pairs = []
    # Iterate through the list of strings
    for i in range(len(my_list)):
        # Get the current string
        curr_str = my_list[i]
        # Check if the current string is an anagram
        if len(curr_str) > 3:
            # Convert the current string to lowercase
            lowercase_str = curr_str.lower()
            # Iterate through the rest of the list of strings
            for j in range(i + 1, len(my_list)):
                # Get the next string
                next_str = my_list[j]
                # Check if the next string is an anagram of the current string
                if lowercase_str == next_str.lower():
                    # Add the pair of strings to the list of anagram pairs
                    anagram_pairs.append((curr_str, next_str))
                    # Increment the count of anagram pairs found
                    count += 1

    # Check if there are at least 276 pairs of anagrams in the given list
    if count >= 276:
        return True
    else:
        return False
