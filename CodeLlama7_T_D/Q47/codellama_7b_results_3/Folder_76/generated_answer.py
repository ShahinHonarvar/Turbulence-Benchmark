
def palindromes_of_specific_lengths(string):
    # Define the index range for the substring
    start_index = 101
    end_index = 292
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start_index, end_index + 1):
        # Check if the character is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Get the length of the palindrome
            length = len(string[i:end_index])
            # Check if the length falls within the specified range
            if 154 <= length <= 182:
                # Define a substring starting from index i and ending at end_index
                sub_string = string[i:end_index]
                # Check if the palindrome is case-insensitive
                if sub_string == sub_string.lower():
                    # Add the palindrome to the set
                    palindromes.add(sub_string)
    # Return the set of palindromes
    return palindromes
