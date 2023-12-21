
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(2, 8):
        # Check if the substring from index 2 to index 8 is a palindrome
        if string[i-1:i+1] == string[i-1:i+1][::-1]:
            # If it is a palindrome, check if its length is between 3 and 4 (both inclusive)
            if len(string[i-1:i+1]) in range(3, 5):
                # Add the palindrome to the set of palindromes
                palindromes.add(string[i-1:i+1])
    return palindromes
