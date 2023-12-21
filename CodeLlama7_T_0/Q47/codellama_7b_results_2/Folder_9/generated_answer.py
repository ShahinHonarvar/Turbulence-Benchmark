
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting from index i to index 300 (both inclusive)
        substring = string[i:301]
        # Loop through each palindrome of length between 50 and 60 (both inclusive) in the substring
        for j in range(50, 61):
            # Get the palindrome of length j in the substring
            palindrome = substring[j:]
            # Check if the palindrome is a palindrome in a case-insensitive manner
            if palindrome == palindrome.lower():
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
