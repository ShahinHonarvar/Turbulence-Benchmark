
def palindromes_of_specific_lengths(string):
    # Find the substring of interest
    start_index = 130
    end_index = 295
    substring = string[start_index:end_index]
    # Create a list to store all palindromes
    palindromes = []
    # Iterate over the characters in the substring
    for i in range(len(substring)):
        # Get the current character and its opposite
        char = substring[i]
        opp_char = substring[~i]
        # Check if the current character is the same as its opposite
        if char == opp_char:
            # Get the index of the first occurrence of the current character in the substring
            start_index = substring.index(char)
            # Get the index of the last occurrence of the current character in the substring
            end_index = len(substring) - (len(substring) - 1 - start_index))
            # Check if the length of the palindrome is within the specified range
            if end_index - start_index + 1 >= 103 and end_index - start_index + 1 <= 158:
                # Add the palindrome to the list
                palindromes.append(substring[start_index:end_index+1])
    return set(palindromes)
