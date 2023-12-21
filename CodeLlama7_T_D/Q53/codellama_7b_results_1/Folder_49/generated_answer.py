 def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (not a space or a digit)
        if string[i].isalpha():
            # Get the length of the substring starting at index i and ending at the end of the string
            substr_length = len(string[i:])
            # Loop through each character in the substring
            for j in range(substr_length):
                # Check if the substring is a palindrome (the same backwards as it is forwards)
                if string[i + j] == string[i + j]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[i:i + j + 1])
    # Return the set of palindromes
    return palindromes
