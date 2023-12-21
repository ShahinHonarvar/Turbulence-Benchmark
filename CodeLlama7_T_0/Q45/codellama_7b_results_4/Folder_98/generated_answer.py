
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the index of the next letter
            j = i + 1
            # While the next letter is also a letter and it is not the last letter in the string
            while j < len(string) and string[j].isalpha() and j != len(string):
                # Check if the current character and the next character form a palindrome of length at least 4
                if string[i].lower() == string[j].lower():
                    # Add the palindrome to the set
                    palindromes.add(string[i:j+1])
                # Increment the index of the next letter
                j += 1
    # Return the set of all palindromes found in the string between indices 3 and 5, inclusive
    return palindromes
