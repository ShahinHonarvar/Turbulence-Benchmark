
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the length of the substring starting from the current character and going to the end of the string
            substr_len = len(string) - i
            # Loop through each possible palindrome length between n and substr_len
            for j in range(n, substr_len + 1):
                # Get the substring of length j starting from the current character
                substr = string[i:i+j]
                # Check if the substring is a palindrome
                if substr == substr[::-1]:
                    # Add the palindrome to the set
                    palindromes.add(substr)
    return palindromes
