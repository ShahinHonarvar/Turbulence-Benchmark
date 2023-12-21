 def palindrome_of_length_at_least_n(input_string, n=3):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each word in the input string
    for word in input_string.split():
        # Check if the word is at least 3 characters long
        if len(word) < n:
            continue

        # Create a copy of the word to check if it's a palindrome
        reversed_word = word[::-1]
        # Check if the word and its reverse are equal
        if word == reversed_word:
            # Add the word to the set of palindromes
            palindromes.add(word)
    return palindromes
