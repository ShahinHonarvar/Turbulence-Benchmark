
def palindromes_of_specific_lengths(string):
    # Define the substring range for consideration
    start = 18
    end = 98
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start, end + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the length of the palindrome
            length = end - start + 1
            # Check if the length is within the specified range
            if length >= 31 and length <= 51:
                # Initialize an empty string to store the palindrome
                palindrome = ""
                # Iterate over the characters in the substring
                for j in range(start, end + 1):
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
