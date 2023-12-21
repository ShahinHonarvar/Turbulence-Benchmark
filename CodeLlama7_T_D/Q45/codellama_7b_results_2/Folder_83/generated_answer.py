
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(2, len(string) - 9 + 1):
        # Check if the current character is a vowel
        if string[i] in "aeiou":
            # Get the indices of all characters before and after the current character
            left_indices = [j for j in range(i - 2, i + 1) if 0 <= j < len(string)]
            right_indices = [j for j in range(i + 3, i + 11) if 0 <= j < len(string)]
            # Loop through each combination of left and right indices
            for left_index in left_indices:
                for right_index in right_indices:
                    # Check if the current combination of left and right indices forms a palindrome
                    if string[left_index] == string[right_index]:
                        # Add the palindrome to the set
                        palindromes.add(string[left_index] + string[right_index])
    # Return the set of all palindromes found in the given string
    return palindromes
