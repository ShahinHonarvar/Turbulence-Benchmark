
def palindromes_of_specific_lengths(string):
    # Define the index range for the substring
    start_index = 15
    end_index = 86
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the left and right indices for the current palindrome
            left = i - (len(string) - end_index) // 2
            right = i + (len(string) - end_index) // 2
            # Check if the current palindrome has a length within the specified range
            if len(string[left:right]) in range(51, 61):
                # Add the current palindrome to the set of palindromes
                palindromes.add(string[left:right].lower())
    # Return the set of palindromes
    return palindromes
