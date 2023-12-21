
def palindromes_of_specific_lengths(string):
    # Create a substring of the specified index range
    substring = string[103:276]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(len(substring)):
        # Check if the character is a letter (i.e., it is not a space or other non-letter character)
        if substring[i].isalpha():
            # Create a copy of the substring starting from index i
            substr = substring[i:]
            # Check if the copy is a palindrome
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
    return palindromes
