
def palindromes_of_specific_lengths(string):
    # Lowercase the string for case-insensitive search
    string = string.lower()
    # Define the index range and palindrome lengths to consider
    index_range = slice(11, 83)
    min_length = 13
    max_length = 66
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the specified index range
    for i in range(*index_range.indices(len(string)))):
        # Check if the current character is a letter (a-z or A-Z)
        if string[i].isalpha():
            # Define a variable to store the length of the palindrome starting at index i
            length = 0
            # Iterate over the characters in the range [i, len(string))
            for j in range(i, len(string)):
                # Check if the current character is a letter (a-z or A-Z) and is not equal to the previous character
                if string[j].isalpha() and string[j] != string[j-1]:
                    # Increment the length of the palindrome by 1
                    length += 1
            # Check if the length of the palindrome is within the specified range
            if min_length <= length <= max_length:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[i:i+length])
    return palindromes
