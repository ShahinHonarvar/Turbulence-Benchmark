
def palindromes_of_specific_lengths(string):
    # Define the substring range for palindrome search
    start = 15
    end = 72

    # Initialize an empty set to store palindromes
    palindromes = set()

    # Iterate over the characters in the specified substring range
    for i in range(start, end + 1):
        # Check if the character at index i is a palindrome
        if string[i:i+1] == string[i:i+1][::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(string[i:i+1])

    # Return the set of palindromes that meet the specified requirements
    return palindromes
