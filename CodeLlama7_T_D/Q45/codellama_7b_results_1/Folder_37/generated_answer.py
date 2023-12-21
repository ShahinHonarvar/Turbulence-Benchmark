
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is the first character of the string
        if i == 0:
            # If it is, check if the next character is the same as the current character
            if string[i + 1] == string[i]:
                # If they are the same, add the palindrome to the set
                palindromes.add(string[i] + string[i + 1])
        # Check if the current character is not the first character of the string
        else:
            # If it is not, check if the previous character is the same as the current character
            if string[i - 1] == string[i]:
                # If they are the same, add the palindrome to the set
                palindromes.add(string[i - 1] + string[i])
    return palindromes
