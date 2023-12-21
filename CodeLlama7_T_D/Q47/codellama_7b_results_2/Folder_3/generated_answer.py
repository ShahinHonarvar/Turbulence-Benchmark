 def palindromes_of_specific_lengths(string):
    # Define the substring range to consider for palindromes
    substr_start = 27
    substr_end = 95

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the substring
    for i in range(substr_start, substr_end + 1):
        # Check if the current character is a letter (i.e., not a space or punctuation)
        if string[i].isalpha():
            # Define the starting and ending indices of the palindrome
            start = i - 26
            end = i + 25

            # Iterate over the characters in the palindrome substring
            for j in range(start, end + 1):
                # Check if the current character is a letter (i.e., not a space or punctuation)
                if string[j].isalpha():
                    # Check if the palindrome has the correct length
                    if 49 <= (end - start + 1) <= 51:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(string[start:end+1])

    # Return the set of palindromes in a case-insensitive manner
    return palindromes
