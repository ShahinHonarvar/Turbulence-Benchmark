
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each letter in the string
    for i in range(6, 9):
        # Check if the current letter is a vowel
        if string[i].lower() in ["a", "e", "i", "o", "u"]:
            # Create a palindrome by mirroring the vowel
            palindrome = ""
            for j in range(i - 1, -1, -1):
                if j == i - 1:
                    palindrome += string[j].lower()
                else:
                    palindrome += string[j + 1].lower()
            # Add the palindrome to the set
            palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
