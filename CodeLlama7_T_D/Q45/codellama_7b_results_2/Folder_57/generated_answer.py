
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a vowel
        if string[i].lower() in "aeiou":
            # Get the index of the next vowel
            next_vowel = i + 1
            while next_vowel < len(string) and string[next_vowel].lower() not in "aeiou":
                # Increment the index of the next vowel
                next_vowel += 1
            # Check if there is a vowel after the current vowel
            if next_vowel < len(string):
                # Get the substring starting from the current vowel and ending with the next vowel
                substring = string[i:next_vowel + 1]
                # Check if the substring is a palindrome
                if substring == substring[::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
