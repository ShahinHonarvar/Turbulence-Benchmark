
def palindromes_of_specific_lengths(string):
    # Define the substring range
    start = 17
    end = 72
    # Define the palindrome lengths
    min_len = 50
    max_len = 51
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring range
    for i in range(start, end + 1):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Define the current palindrome length
            len_palindrome = end - start + 1
            # Check if the current palindrome length falls within the specified range
            if min_len <= len_palindrome <= max_len:
                # Define the current palindrome string
                palindrome_str = string[start:end+1]
                # Check if the current palindrome string is a palindrome in a case-insensitive manner
                if palindrome_str == palindrome_str[::-1]:
                    # Add the current palindrome string to the set of palindromes
                    palindromes.add(palindrome_str)
    # Return the set of palindromes
    return palindromes
