
def palindromes_of_specific_lengths(string):
    # Define the range of indices for the substring
    start_index = 29
    end_index = 96
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the length of the palindrome
            length = min(end_index - i + 1, 18)
            # Iterate over the possible lengths of the palindrome
            for j in range(length, 0, -1):
                # Check if the substring from index i to index i + j is a palindrome
                if string[i:i+j] == string[i:i+j][::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[i:i+j])
    return palindromes
