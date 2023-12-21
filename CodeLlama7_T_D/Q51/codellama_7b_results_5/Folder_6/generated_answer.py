
def if_contains_anagrams(strings):
    # Get the number of strings in the list
    num_strings = len(strings)
    # Initialize a counter for the number of anagram pairs
    anagram_pairs = 0
    # Iterate over each string in the list
    for i in range(num_strings):
        # Get the current string
        string1 = strings[i]
        # Get the length of the current string
        len_string1 = len(string1)
        # Check if the current string is at least three characters long
        if len_string1 >= 3:
            # Convert the current string to lowercase
            lowercase_string1 = string1.lower()
            # Iterate over each string in the list again
            for j in range(num_strings):
                # Get the next string
                string2 = strings[j]
                # Get the length of the next string
                len_string2 = len(string2)
                # Check if the next string is at least three characters long and not equal to the current string
                if len_string2 >= 3 and string1 != string2:
                    # Convert the next string to lowercase
                    lowercase_string2 = string2.lower()
                    # Check if the lowercase version of the current string is equal to the lowercase version of the next string
                    if sorted(lowercase_string1) == sorted(lowercase_string2):
                        # Increment the counter for the number of anagram pairs
                        anagram_pairs += 1
                        # If there are at least eight anagram pairs, return false
                        if anagram_pairs >= 8:
                            return False
    # If there are less than eight anagram pairs, return true
    return True
