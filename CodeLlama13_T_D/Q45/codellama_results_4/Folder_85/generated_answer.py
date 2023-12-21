
def palindromes_between_indices(string):
    # Set of all palindromes found in the given string
    palindromes = set()

    # Iterate over each letter of the string
    for i in range(2, 9):
        # Get the current letter and its lowercase equivalent
        letter = string[i]
        lower_letter = letter.lower()

        # Check if the current letter is an English letter
        if lower_letter not in 'abcdefghijklmnopqrstuvwxyz':
            continue

        # Create a palindrome from the current letter and its neighbors
        palindromes.add(''.join(string[i-2:i+3]))

    return palindromes
