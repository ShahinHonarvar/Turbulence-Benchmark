
def palindromes_of_specific_lengths(string):
    # Define the required parameters
    min_len = 3
    max_len = 7
    substring_range = range(1, 10)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in substring_range:
        # Get the character at index i
        char = string[i]
        # If the character is not a letter, skip to the next iteration
        if not char.isalpha():
            continue

        # Iterate over the characters in the reversed substring
        for j in range(i, -1, -1):
            # Get the character at index j
            rev_char = string[j]
            # If the character is not a letter, skip to the next iteration
            if not rev_char.isalpha():
                continue

            # Check if the character and its reverse are equal
            if char == rev_char:
                # If the length of the palindrome is between 3 and 7 (both inclusive), add it to the set of palindromes
                if len(string[i:j+1]) in range(min_len, max_len+1):
                    palindromes.add(string[i:j+1])
    # Return the set of palindromes found
    return palindromes
