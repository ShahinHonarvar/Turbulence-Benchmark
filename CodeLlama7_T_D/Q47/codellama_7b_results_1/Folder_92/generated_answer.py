 def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting from index i to index 4 (both inclusive)
        substr = string[i:i+5]
        # Loop through each palindrome of length between 3 and 4 (both inclusive) in the substring
        for j in range(3, 5):
            # Check if the palindrome is found in the substring
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
    return palindromes
