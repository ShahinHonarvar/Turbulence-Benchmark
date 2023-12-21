
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each character in the string
    for i in range(1, len(string) - 1):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a list of all letters between the current index and index 7
            letters = [string[j] for j in range(i, min(len(string), i + 7))]]
            # Iterate through each possible arrangement of the letters
            for combination in combinations(letters, len(letters)):
                # Check if the current combination is a palindrome
                if ''.join(combination).lower() == ''.join(combination)[::-1].lower():
                    # Add the palindrome to the set
                    palindromes.add(''.join(combination))
    # Return the set of palindromes
    return palindromes
