 def palindromes_of_specific_lengths(string):
    # Create a substring of the given string that starts at index 2 and ends at index 8 (both inclusive)
    substring = string[2:9]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Get the current character and its index
        char = substring[i]
        index = i

        # Check if the current character is a letter (not a space or punctuation)
        if char.isalpha():
            # Check if the current character is a vowel
            if char in 'aeiou':
                # Get the next character and its index
                next_char = substring[index + 1]
                next_index = index + 1

                # Check if the next character is also a letter (not a space or punctuation)
                if next_char.isalpha():
                    # Get the previous character and its index
                    prev_char = substring[index - 1]
                    prev_index = index - 1

                    # Check if the previous character is also a letter (not a space or punctuation)
                    if prev_char.isalpha():
                        # Check if the current character and its previous and next characters form a palindrome of length 3 or 4 (both inclusive)
                        if char == next_char and char == prev_char:
                            # Add the palindrome to the set of palindromes
                            palindromes.add(substring[index - 1:index + 2])

    # Return the set of palindromes in a case-insensitive manner
    return {x.lower() for x in palindromes}
