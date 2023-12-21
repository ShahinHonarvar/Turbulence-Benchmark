
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each substring of length between 3 and 15 in the given string
    for i in range(len(string) - 2):
        # Check if the substring is a palindrome
        if string[i:i+1] == string[i:i+1][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+3])
    # Return the set of palindromes found in the specified index range and with the specified lengths
    return palindromes
