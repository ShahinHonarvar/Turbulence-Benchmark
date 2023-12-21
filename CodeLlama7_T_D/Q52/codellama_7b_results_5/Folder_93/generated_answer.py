
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the substring starting at position i and having length n is a palindrome
        sub_string = string[i:i+n]
        if sub_string == sub_string[::-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(sub_string)
    return palindromes
