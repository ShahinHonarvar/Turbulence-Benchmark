
def palindromes_of_specific_lengths(string):
    # Define the index range for the substring search
    start_index = 32
    end_index = 71
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the length of the palindrome
            length = min(end_index - i + 1, 32)
            # Iterate over the characters in the substring starting from i and ending at i + length - 1
            for j in range(i, i + length):
                # Check if the character at index j is a letter
                if string[j].isalpha():
                    # Define the palindrome as the substring starting from i and ending at i + length - 1
                    palindrome = string[i:i + length]
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    return palindromes
