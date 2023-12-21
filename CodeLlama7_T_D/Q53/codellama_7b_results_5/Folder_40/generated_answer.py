
def palindrome_of_length_at_least_n(s, n):
    # Convert the string to lowercase
    s = s.lower()
    # Create a set to store the palindromes
    palindromes = set()
    # Iterate over each word in the string
    for word in s.split():
        # Check if the word is at least n characters long
        if len(word) < n:
            continue

        # Check if the word is a palindrome
        if word == word[::-1]:
            # Add the word to the set of palindromes
            palindromes.add(word)
    # Return the set of palindromes
    return palindromes
