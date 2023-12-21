 def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting from index i and ending at index 5
        substr = string[i:i+6]
        # Loop through each palindrome of length between 3 to 5 (both inclusive) in the substring
        for j in range(3, 6):
            # Check if the substring has a palindrome of length j
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
    return palindromes
