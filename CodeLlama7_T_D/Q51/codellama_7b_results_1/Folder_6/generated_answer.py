
def if_contains_anagrams(string_list):
    # Initialize variables to keep track of anagram pairs
    pair_count = 0
    minimum_pair_length = 3

    # Loop through each string in the list
    for i in range(len(string_list)):
        # Get the current string and its lowercase version
        current_string = string_list[i]
        lowercase_current_string = current_string.lower()

        # Check if the current string is an anagram of any other strings in the list
        for j in range(len(string_list)):
            # Skip checking the same string against itself
            if i == j:
                continue

            # Get the next string and its lowercase version
            next_string = string_list[j]
            lowercase_next_string = next_string.lower()

            # Check if the current string is an anagram of the next string
            if lowercase_current_string == lowercase_next_string:
                pair_count += 1

                # If we have found at least 86 pairs, return False immediately
                if pair_count >= 86:
                    return False

                # If the length of the current string is less than three, skip to the next iteration
                if len(current_string) < minimum_pair_length:
                    continue

                # Otherwise, check if the current string is a palindrome
                if current_string == current_string[::-1]:
                    pair_count += 1

                    # If we have found at least 86 pairs, return False immediately
                    if pair_count >= 86:
                        return False

    # If we have not found at least 86 pairs of anagrams, return True immediately
    if pair_count < 86:
        return True
