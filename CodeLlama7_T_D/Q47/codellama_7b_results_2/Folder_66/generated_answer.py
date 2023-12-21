
def palindromes_of_specific_lengths(string):
    # Define the substring range
    start = 32
    end = 79

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the specified substring
    for i in range(start, end + 1):
        # Check if the character is a letter (lowercase or uppercase)
        if string[i].isalpha():
            # Convert the character to lowercase
            char = string[i].lower()

            # Iterate over the possible palindrome lengths
            for length in range(35, 42):
                # Check if the substring starting at index i and having a length of length is a palindrome
                if char == string[i + length - 1].lower():
                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[i:i + length])

    return palindromes
