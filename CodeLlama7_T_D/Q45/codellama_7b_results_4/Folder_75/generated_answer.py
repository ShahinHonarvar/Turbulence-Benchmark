
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible starting index of a palindrome
    for i in range(2, len(string)):
        # Loop through each possible ending index of a palindrome
        for j in range(i + 1, len(string) + 1):
            # Check if the substring between the starting and ending indices is a palindrome
            if string[i:j].lower() == string[i:j][::-1].lower():
                # If it is a palindrome, add it to the set of palindromes
                palindromes.add(string[i:j])
    # Return the set of palindromes
    return palindromes
