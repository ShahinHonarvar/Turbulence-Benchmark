 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of a palindrome between indices 1 and 4
    for length in range(3, len(string)):
        # Loop through each possible starting index of a palindrome between indices 1 and 4
        for start_index in range(1, len(string) - length + 2):
            # Initialize an empty string to store the current palindrome
            current_palindrome = ""
            # Loop through each character of the current palindrome
            for i in range(start_index, start_index + length):
                # Add the character to the current palindrome
                current_palindrome += string[i]
            # If the current palindrome is a valid palindrome, add it to the set of palindromes
            if current_palindrome == current_palindrome[::-1]:
                palindromes.add(current_palindrome)
    # Return the set of palindromes
    return palindromes
