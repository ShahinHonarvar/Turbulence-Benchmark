
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting at index i and ending at index len(string) - 1 (inclusive)
        sub_string = string[i:len(string)]
        # Check if the substring is a palindrome
        if sub_string == sub_string[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(sub_string)
    # Return the set of palindromes
    return palindromes
