
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the possible combinations of letters between indices 1 and 7
    for i in range(1, len(string) - 6):
        for j in range(i + 1, len(string) - 5):
            word = string[i:j+1]
            # Check if the word is a palindrome
            if word == word[::-1]:
                # Add the word to the set of palindromes
                palindromes.add(word)
    return palindromes
