
def if_contains_anagrams(my_list):
    # Define a function to check if two strings are anagrams
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    # Initialize a counter for the number of pairs of anagrams found
    num_pairs = 0
    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        str1 = my_list[i]
        # Check if the current string is at least three characters long
        if len(str1) >= 3:
            # Convert the current string to lowercase
            str1_lower = str1.lower()
            # Iterate over the remaining strings in the list
            for j in range(i + 1, len(my_list)):
                # Get the next string
                str2 = my_list[j]
                # Check if the next string is at least three characters long
                if len(str2) >= 3:
                    # Convert the next string to lowercase
                    str2_lower = str2.lower()
                    # Check if the current and next strings are anagrams of each other
                    if is_anagram(str1_lower, str2_lower):
                        # Increment the counter for the number of pairs of anagrams found
                        num_pairs += 1
                        # If the counter reaches 188, return True to indicate that there are at least 188 pairs of anagrams in the list
                        if num_pairs == 188:
                            return True
    # If the counter does not reach 188, return False to indicate that there are no more than 187 pairs of anagrams in the list
    return False
