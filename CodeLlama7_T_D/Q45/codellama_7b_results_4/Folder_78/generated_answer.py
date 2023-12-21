
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(6, 9):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the indices of the current letter in the string
            indices = [j for j, char in enumerate(string) if char == string[i]]
            # Loop through each index of the current letter
            for k in range(len(indices)):
                # Check if the current letter is a vowel or not
                if string[indices[k]].lower() in ["a", "e", "i", "o", "u"]:
                    # Get the indices of the previous and next letters in the string
                    prev_index = indices[k] - 1
                    next_index = indices[k] + 1
                    # Check if the current letter is the first or last letter in the string
                    if prev_index < 0 or next_index >= len(string):
                        # Add the palindrome to the set
                        palindromes.add(string[i])
                    # Check if the previous and next letters are vowels or not
                    elif string[prev_index].lower() in ["a", "e", "i", "o", "u"] and string[next_index].lower() in ["a", "e", "i", "o", "u"]:
                        # Add the palindrome to the set
                        palindromes.add(string[i])
    # Return the set of all palindromes
    return palindromes
