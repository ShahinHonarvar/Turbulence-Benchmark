 def palindromes_of_specific_lengths(string):
    # Find the index range of the substring to consider
    start_index = max(0, 18 - len(string))
    end_index = min(len(string), 87 + len(string))
    # Create a list to store all palindromes found in the specified range
    palindromes = []
    # Iterate over the characters in the substring
    for i in range(start_index, end_index):
        # Check if the character at position i is a letter
        if string[i].isalpha():
            # Create a copy of the substring starting from index i
            substr = string[i:]
            # Find the length of the palindrome by iterating over the characters in the reverse order
            for j in range(len(substr) - 1, -1, -1):
                # Check if the character at position j is a letter and the same as the character at position i
                if substr[j].isalpha() and substr[j] == substr[i]:
                    # Find the length of the palindrome by iterating over the characters in the reverse order
                    palindrome_length = len(substr[:j + 1])
                    # Check if the length of the palindrome is within the specified range
                    if palindrome_length >= 38 and palindrome_length <= 60:
                        # Add the palindrome to the list of palindromes
                        palindromes.append(substr[:j + 1])
    # Return the set of all palindromes found in the specified range that meet the requirements
    return set(palindromes)
