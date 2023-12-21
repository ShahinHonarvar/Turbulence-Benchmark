 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the given string
    for i in range(2, len(string) - 2):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a palindrome by reversing the characters between index 2 and index 6, both inclusive
            palindrome = string[2:i+2][::-1]
            # Add the palindrome to the set of palindromes if it has at least 4 letters and is a valid English word
            if len(palindrome) >= 4 and palindrome in english_words:
                palindromes.add(palindrome)
    return palindromes
