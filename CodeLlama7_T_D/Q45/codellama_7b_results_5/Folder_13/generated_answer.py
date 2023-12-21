
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each letter in the string
    for i in range(3, 9 + 1):
        # Check if the current letter is a vowel
        if string[i] in "aeiou":
            # If it is, add its mirrored version to the set of palindromes
            palindromes.add(string[i].lower() + string[i].upper())
    # Return the set of palindromes
    return palindromes
