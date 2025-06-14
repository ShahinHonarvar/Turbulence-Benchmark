
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(2, len(string) - 1):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the indices of the current character in the string
            indices = [j for j, x in enumerate(string) if x == string[i]]
            # Loop through each index of the current character
            for j in indices:
                # Check if the current character is a letter and its index is between 2 and 7 (inclusive)
                if string[j].isalpha() and 2 <= j <= 7:
                    # Get the palindrome by reversing the characters of the substring starting at index j and ending at index i
                    palindrome = string[j:i][::-1]
                    # Add the palindrome to the set if it has a length of at least 6
                    if len(palindrome) >= 6:
                        palindromes.add(palindrome)
    return palindromes
