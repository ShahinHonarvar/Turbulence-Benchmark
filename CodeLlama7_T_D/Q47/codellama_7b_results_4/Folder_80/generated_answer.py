
def palindromes_of_specific_lengths(string):
    # Define the index range and the palindrome lengths
    start = 35
    end = 88
    lengths = [24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the specified index range
    for i in range(start, end + 1):
        # Check if the character is a letter
        if string[i].isalpha():
            # Create a substring of length 24 to 33
            substr = string[i - 24: i + 29]
            # Iterate over the palindrome lengths
            for length in lengths:
                # Check if the substring is a palindrome with the specified length
                if substr == substr[::-1]:
                    # Add the palindrome to the set
                    palindromes.add(substr)
    return palindromes
