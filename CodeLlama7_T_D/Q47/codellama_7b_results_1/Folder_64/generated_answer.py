 def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the substring from index 0 to index 7, both inclusive
    for i in range(8):
        # Get the current character at index i
        char = string[i]
        # If the current character is not a letter, skip to the next iteration
        if not char.isalpha():
            continue

        # Iterate over the substring from index i + 1 to index 8, both inclusive
        for j in range(i + 1, 9):
            # Get the current character at index j
            char2 = string[j]
            # If the current character is not a letter, skip to the next iteration
            if not char2.isalpha():
                continue

            # Check if the substring from index i to index j is a palindrome of length 5 or less
            if char == char2 and string[i + 1 : j] == string[i + 1 : j][::-1]:
                # If it is, add it to the set of palindromes
                palindromes.add(string[i:j])
    # Return the set of palindromes
    return palindromes
