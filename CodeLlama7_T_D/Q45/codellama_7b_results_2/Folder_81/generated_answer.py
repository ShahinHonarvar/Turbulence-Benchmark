
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each letter in the string
    for i in range(len(string)):
        # Get the current letter and its index
        letter = string[i]
        index = i

        # Loop through each letter in the string starting from the next letter
        for j in range(index + 1, len(string)):
            # Get the current letter and its index
            letter2 = string[j]
            index2 = j

            # Check if the two letters are the same case-insensitive
            if letter.lower() == letter2.lower():
                # Create a palindrome by combining the two letters
                palindrome = f"{letter}{letter2}"

                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)

    return palindromes
