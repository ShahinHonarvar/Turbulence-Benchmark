
def palindromes_of_specific_lengths(string):
    # Define the index range and palindrome length requirements
    start_index = 0
    end_index = 30
    min_palindrome_length = 20
    max_palindrome_length = 30
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the substring starting from index i and ending at the end of the string
            substr = string[i:]
            # Iterate over the characters in the substring
            for j in range(0, len(substr)):
                # Check if the character at index j is a letter
                if substr[j].isalpha():
                    # Define the palindrome as the substring starting from index i and ending at index j
                    palindrome = substr[i:j + 1]
                    # Check if the palindrome length is within the specified range
                    if len(palindrome) >= min_palindrome_length and len(palindrome) <= max_palindrome_length:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
