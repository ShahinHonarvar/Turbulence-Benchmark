
def palindrome_of_length_at_least_n(input_string, n):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each word in the input string
    for word in input_string.split():
        # Check if the word is at least n characters long
        if len(word) >= n:
            # Convert the word to lowercase
            word = word.lower()
            # Check if the word is a palindrome
            if word == word[::-1]:
                # Add the palindrome to the set
                palindromes.add(word)
    # Return the set of palindromes
    return palindromes
