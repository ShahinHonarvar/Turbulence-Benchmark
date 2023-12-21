
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(4, 6):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a list of all letters between index 4 and index 5
            letters = [string[j] for j in range(4, 6)]
            # Add each palindrome to the set
            for palindrome in ["".join(letters)]:
                palindromes.add(palindrome)
    return palindromes
