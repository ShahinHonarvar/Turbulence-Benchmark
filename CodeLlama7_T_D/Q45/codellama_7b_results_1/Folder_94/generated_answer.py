
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(3, len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the indices of all letters before and after the current letter
            before_indices = [j for j in range(i) if string[j].isalpha()]
            after_indices = [j for j in range(i + 1, len(string)) if string[j].isalpha()]
            # Loop through each combination of before and after indices
            for before_index in before_indices:
                for after_index in after_indices:
                    # Check if the current letter is between the two given indices
                    if before_index <= i <= after_index:
                        # Get the letters around the current letter
                        before_letter = string[before_index]
                        after_letter = string[after_index]
                        # Check if the current letter is a palindrome
                        if before_letter == after_letter and len(before_letter) >= 3:
                            # Add the palindrome to the set
                            palindromes.add((string[i].lower(), string[i].upper()))
    # Return the set of palindromes
    return palindromes
