
def palindromes_of_specific_lengths(string):
    # Define the index range for the substring
    start = 10
    end = 100
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start, end + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the length of the palindrome
            length = i - start + 1
            # Check if the length is within the specified range
            if length >= 10 and length <= 50:
                # Define the palindrome as a substring of the original string
                palindrome = string[i - length + 1:i + 1]
                # Check if the palindrome is case-insensitive
                if palindrome.lower() == palindrome:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    return palindromes
