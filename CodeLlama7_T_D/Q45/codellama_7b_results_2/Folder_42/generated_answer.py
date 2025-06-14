
def palindromes_between_indices(string):
    # Create a list of all the English letters in the given string
    letters = []
    for char in string:
        if char.isalpha():
            letters.append(char.lower())
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through all possible pairs of letters in the given range
    for i in range(6, 10):
        for j in range(i + 1, len(letters) - 2):
            # Check if the substring starting at index i and ending at index j is a palindrome
            if letters[i:j] == "".join(reversed(letters[i:j])):
                # If it is a palindrome, add it to the set of palindromes
                palindromes.add("".join(reversed(letters[i:j]))))
    return palindromes
