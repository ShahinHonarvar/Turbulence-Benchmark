
def palindromes_of_specific_lengths(string):
    # Create a list of all palindromes in the string
    palindromes = []
    for i in range(len(string)):
        # Check if the character at index 'i' is the same as the character at index 'len(string) - 1 - i'
        if string[i] == string[len(string) - 1 - i]:
            # If it is, create a substring starting at index 'i' and ending at index 'len(string) - 1 - i'
            substr = string[i:len(string) - 1 - i]
            # Check if the length of the substring is between 18 and 21 (both inclusive)
            if len(substr) >= 18 and len(substr) <= 21:
                # Add the substring to the list of palindromes
                palindromes.append(substr)
    return set(palindromes)
