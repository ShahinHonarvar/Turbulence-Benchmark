
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive search
    string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each substring of length 84 in the given string
    for i in range(len(string) - 83):
        # Check if the substring is a palindrome by comparing it with its reversed form
        if string[i:i+84] == string[i:i+84][::-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(string[i:i+84])
    # Return the set of palindromes found in the given string
    return palindromes
