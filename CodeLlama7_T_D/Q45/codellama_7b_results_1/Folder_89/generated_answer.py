
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the indices of all occurrences of the current letter in the string
            indices = [j for j, l in enumerate(string) if l == string[i]]
            # Iterate over each occurrence of the current letter
            for j in indices:
                # Check if the letter is surrounded by letters on both sides
                if 5 <= j < 9 or (j == 0 and 5 <= string[1] <= 8) or (j == len(string) - 1 and 5 <= string[-2] <= 8):
                    # Get the substring that contains the current letter and its surroundings
                    substring = string[max(0, j - 3):min(len(string), j + 4)]]
                    # Check if the substring is a palindrome
                    if substring == substring[::-1]:
                        # Add the palindrome to the set
                        palindromes.add(substring)
    # Return the set of all palindromes found in the string
    return palindromes
