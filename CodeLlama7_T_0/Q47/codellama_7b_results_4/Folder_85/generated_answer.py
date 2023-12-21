
def palindromes_of_specific_lengths(string):
    # Define the substring range for consideration
    start_index = 29
    end_index = 98
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the length of the palindrome
            length = 9 - (i - start_index)
            # Check if the length is within the specified range
            if length >= 6 and length <= 9:
                # Initialize an empty string to store the palindrome
                palindrome = ""
                # Iterate over the characters in the substring
                for j in range(i - (length // 2), i + (length // 2) + 1):
                    # Check if the character at index j is a letter
                    if string[j].isalpha():
                        # Add the character to the palindrome string
                        palindrome += string[j]
                # Check if the palindrome is case-insensitive and only consists of English letters
                if palindrome.lower() == palindrome and palindrome.isalpha():
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
