
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(4, 10):
        # Check if the current character is a vowel or not
        if string[i] in "aeiou":
            # If it's a vowel, check if there are any other vowels before and after it
            if string[i - 1] in "aeiou" and string[i + 1] in "aeiou":
                # If there are, create a palindrome by concatenating the current character with the characters before and after it
                palindrome = string[i - 1] + string[i] + string[i + 1]
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
