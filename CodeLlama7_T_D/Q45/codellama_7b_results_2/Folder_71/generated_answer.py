
def palindromes_between_indices(s):
    # Create a list of all English letters in the given string
    letters = [chr(i) for i in range(97, 123)]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each letter in the given string
    for letter in s:
        # If the letter is not in the list of English letters, continue to the next iteration
        if letter not in letters:
            continue

        # Create a copy of the given string and remove all occurrences of the current letter
        temp = s.replace(letter, "")

        # Iterate over each letter in the modified string
        for letter2 in temp:
            # If the letter is not in the list of English letters, continue to the next iteration
            if letter2 not in letters:
                continue

            # Create a copy of the modified string and remove all occurrences of the current letter
            temp = temp.replace(letter2, "")

            # If the length of the modified string is at least 4, add it to the set of palindromes
            if len(temp) >= 4:
                palindromes.add(temp)

    # Return the set of palindromes in a case-insensitive manner
    return frozenset(palindrome.lower() for palindrome in palindromes)
