
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting at index i and of length 186
        sub_string = string[i:i+186]
        # Check if the substring is a palindrome
        if sub_string == sub_string[::-1]:
            # Add the palindrome to the set
            palindromes.add(sub_string)
    # Return the set of palindromes
    return palindromes
