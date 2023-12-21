
def palindromes_between_indices(string):
    # Create a list of all possible palindromes of length 6 or more
    palindromes = []
    for i in range(2, 9 + 1):
        # Get the substring that corresponds to the current index
        substring = string[i - 1:i + 1]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the substring to the list of palindromes
            palindromes.append(substring)
    return set(palindromes)
