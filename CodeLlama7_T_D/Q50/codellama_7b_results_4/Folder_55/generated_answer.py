
def if_contains_anagrams(str_list):
    # Initialize variables
    anagram_count = 0
    min_length = 3

    # Iterate over the list of strings
    for i in range(len(str_list)):
        # Get the current string
        str1 = str_list[i]
        # Check if the length is greater than or equal to the minimum length
        if len(str1) >= min_length:
            # Convert the current string to lowercase
            str1_lower = str1.lower()
            # Iterate over the rest of the list of strings
            for j in range(i+1, len(str_list)):
                # Get the next string
                str2 = str_list[j]
                # Check if the length is greater than or equal to the minimum length
                if len(str2) >= min_length:
                    # Convert the next string to lowercase
                    str2_lower = str2.lower()
                    # Check if the current string and the next string are anagrams
                    if sorted(str1_lower) == sorted(str2_lower):
                        # Increment the anagram count
                        anagram_count += 1
                        # Break out of the inner loop
                        break

    # Return the result
    return anagram_count >= 15
