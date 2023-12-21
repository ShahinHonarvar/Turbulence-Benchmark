
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(8, 10):
        # Check if the character is a vowel
        if string[i] in "aeiou":
            # If it is a vowel, check if there are any other vowels in the string before and after the current vowel
            for j in range(i - 1, i + 2):
                # Check if the character at index j is a vowel
                if j >= 0 and j < len(string) and string[j] in "aeiou":
                    # If there are any other vowels in the string before and after the current vowel, add the palindrome to the set of palindromes
                    palindromes.add(string[i].lower() + string[j].lower() + string[i].lower())
    # Return the set of palindromes
    return palindromes
