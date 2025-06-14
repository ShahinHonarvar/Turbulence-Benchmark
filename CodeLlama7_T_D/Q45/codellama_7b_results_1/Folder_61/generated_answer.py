
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter (i.e., not a space or punctuation)
        if string[i].isalpha():
            # Loop through each character in the reversed substring starting at index i and ending at index 7 (inclusive)
            for j in range(len(string[i:8])):
                # Check if the current character is a letter (i.e., not a space or punctuation)
                if string[i:8][j].isalpha():
                    # Create a palindrome by reversing the substring starting at index i and ending at index 7 (inclusive)
                    palindrome = string[i:8][::-1]
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    return palindromes
