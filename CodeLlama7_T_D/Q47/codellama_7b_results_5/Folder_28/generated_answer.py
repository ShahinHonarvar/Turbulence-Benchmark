
def palindromes_of_specific_lengths(string):
    # Define the range of indices for the substring
    start_index = 32
    end_index = 71
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the length of the palindrome
            palindrome_length = 32

            # Iterate over the characters in the substring from index i to index i + palindrome_length - 1 (both inclusive)
            for j in range(i, i + palindrome_length):
                # Check if the character at index j is a letter
                if string[j].isalpha():
                    # Define the palindrome
                    palindrome = string[i:j + 1]

                    # Check if the palindrome meets the requirements
                    if len(palindrome) == palindrome_length and palindrome.lower() == palindrome:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)

    return palindromes
