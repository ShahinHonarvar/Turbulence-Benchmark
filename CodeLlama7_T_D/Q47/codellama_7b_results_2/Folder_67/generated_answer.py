
def palindromes_of_specific_lengths(string):
    # Define the substring range and palindrome lengths
    start = 65
    end = 99
    lengths = range(26, 34)

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each character in the substring
    for i in range(start, end + 1):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Iterate over each length in the specified range
            for j in lengths:
                # Check if the current length is greater than or equal to the length of the substring from index i to index i + j - 1
                if j >= len(string[i:i+j])):
                    # Check if the current substring is a palindrome
                    if string[i:i+j] == string[i:i+j][::-1]:
                        # Add the palindrome to the set
                        palindromes.add(string[i:i+j])

    # Return the set of palindromes
    return palindromes
