
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each index in the specified range
    for i in range(20):
        # Calculate the length of the palindrome at this index
        length = min(80, len(string) - i)
        # Check if there is a palindrome of this length at this index
        if string[i:i + length] == string[i:i + length][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i + length])
    return palindromes
