 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(3, len(string) + 1):
        # Generate all possible palindromes of length i using the letters between indices 3 and i
        for j in range(i, len(string) - (i - 3) + 1):
            # Check if the substring starting at index j and ending at index j + i - 1 forms a palindrome
            if string[j:j + i] == string[j:j + i][::-1]:
                # If it does, add it to the set of palindromes
                palindromes.add(string[j:j + i])
    return palindromes
