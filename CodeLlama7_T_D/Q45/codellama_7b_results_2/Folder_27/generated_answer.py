
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(2, len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Get the index of the previous and next letters
            prev_index = i - 1
            next_index = i + 1
            # Check if the previous and next letters are also letters
            if prev_index >= 0 and next_index < len(string) and string[prev_index].isalpha() and string[next_index].isalpha():
                # Get the substring of the original string that forms the palindrome
                palindrome = string[i - 1: i + 2]
                # Add the palindrome to the set
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
