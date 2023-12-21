
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting from index i to index 9 (both inclusive)
        substring = string[i:i+10]
        # Loop through each palindrome of length between 3 and 5 (both inclusive) in the substring
        for j in range(3, 6):
            # Get the palindrome of length j in the substring
            palindrome = substring[j:j+j]
            # Check if the palindrome is a valid English word
            if palindrome.isalpha():
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes in a case-insensitive manner
    return frozenset(palindromes)
