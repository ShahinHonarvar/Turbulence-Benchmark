
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(3, len(string) - 9):
        # Check if the substring from index 3 to index 9 is a palindrome
        if string[i:i+9] == string[i:i+9][::-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(string[i:i+9])
    return palindromes
