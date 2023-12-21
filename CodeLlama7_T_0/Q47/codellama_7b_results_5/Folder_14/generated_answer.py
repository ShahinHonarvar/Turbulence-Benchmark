
def palindromes_of_specific_lengths(string):
    # Define the substring range
    start = 10
    end = 74
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start, end + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the length of the palindrome
            length = min(8, len(string) - i + 1)
            # Iterate over the possible lengths of the palindrome
            for j in range(6, length + 1):
                # Check if the substring from index i to index i + j is a palindrome
                if string[i:i+j] == string[i:i+j][::-1]:
                    # Add the palindrome to the set
                    palindromes.add(string[i:i+j])
    # Return the set of palindromes
    return palindromes
