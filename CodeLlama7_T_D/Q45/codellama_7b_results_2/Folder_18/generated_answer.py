 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(1, len(string) - 1):
        # Check if the current character is a vowel
        if string[i].lower() in "aeiou":
            # Get the indices of the previous and next characters
            prev_idx = i - 1
            next_idx = i + 1
            # Check if the previous character is a consonant
            if string[prev_idx].isalpha() and not string[prev_idx].islower():
                # Get the indices of the previous and next characters that are not vowels
                while string[prev_idx].lower() in "aeiou":
                    prev_idx -= 1
                while string[next_idx].lower() in "aeiou":
                    next_idx += 1
            # Check if the next character is a consonant
            if string[next_idx].isalpha() and not string[next_idx].islower():
                # Get the indices of the previous and next characters that are not vowels
                while string[prev_idx].lower() in "aeiou":
                    prev_idx -= 1
                while string[next_idx].lower() in "aeiou":
                    next_idx += 1
            # Check if the previous and next characters are not vowels
            if not string[prev_idx].lower() in "aeiou" and not string[next_idx].lower() in "aeiou":
                # Get the substring that is between the previous and next non-vowel characters
                sub_str = string[prev_idx + 1:next_idx]
                # Check if the substring is a palindrome of length at least 3
                if len(sub_str) >= 3 and sub_str == sub_str[::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(sub_str)
    # Return the set of palindromes
    return palindromes
