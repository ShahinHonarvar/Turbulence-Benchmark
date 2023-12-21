 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each index in the specified range
    for i in range(2, 9):
        # Generate all possible palindromes of length at least 4 using the English letters between indices i and 8 (inclusive)
        for j in range(i, 9):
            # Check if the substring starting from index i and ending at index j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # If it is a palindrome, add it to the set of palindromes
                palindromes.add(string[i:j])
    return palindromes
