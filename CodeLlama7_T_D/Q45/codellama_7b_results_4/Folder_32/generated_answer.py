
def palindromes_between_indices(string):
    # Create a list of all the English letters in the given string
    letters = []
    for char in string:
        if char.isalpha():
            letters.append(char)

    # Create a set to store all the palindromes

    palindromes = set()

    # Iterate over each letter in the given string

    for i in range(len(letters)):

        # Iterate over each letter in the given string starting from the next letter of the current letter

        for j in range(i + 1, len(letters)):

            # Create a list of letters from the current letter to the next letter

            substring = letters[i:j]

            # Check if the substring is a palindrome

            if substring == substring[::-1]:

                # Add the substring to the set of palindromes

                palindromes.add(''.join(substring))

    return palindromes
