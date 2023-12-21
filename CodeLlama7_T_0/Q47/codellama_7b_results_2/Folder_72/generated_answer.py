
def palindromes_of_specific_lengths(string):
    # Define the substring range for palindromes
    start_index = 26
    end_index = 90
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string within the specified range
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a letter (not a space or punctuation)
        if string[i].isalpha():
            # Define the palindrome as the substring starting from index i and ending at index i
            palindrome = string[i:i+1]
            # Check if the palindrome is of length between 27 to 58 (both inclusive)
            if len(palindrome) >= 27 and len(palindrome) <= 58:
                # Add the palindrome to the set
                palindromes.add(palindrome)
    # Return the set of palindromes in a case-insensitive manner
    return {x.lower() for x in palindromes}
