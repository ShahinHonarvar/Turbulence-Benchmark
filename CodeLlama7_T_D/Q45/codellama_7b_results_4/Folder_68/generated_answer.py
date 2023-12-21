
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each index in the string
    for i in range(1, len(string)):
        # Check if the character at index i is not a space or a punctuation mark
        if string[i] not in [" ", ".", ",", ";", ":", "?", "!"]:
            # Loop through each index in the reversed substring starting from i + 1
            for j in range(i + 1, len(string)):
                # Check if the character at index j is not a space or a punctuation mark
                if string[j] not in [" ", ".", ",", ";", ":", "?", "!"]:
                    # Create a palindrome by reversing the substring starting from i + 1 to j
                    palindrome = string[i + 1:j][::-1]
                    # Check if the palindrome has at least 4 characters and add it to the set of palindromes
                    if len(palindrome) >= 4:
                        palindromes.add(palindrome)
    return palindromes
