
def palindrome_of_length_at_least_n(string, n=62):
    # Create a list of all possible palindromes
    palindromes = []
    for i in range(len(string) - n + 1):
        # Get the substring starting at index i and ending at index i + n - 1
        sub_str = string[i:i + n]
        # Check if the substring is a palindrome
        if sub_str == sub_str[::-1]:
            # Add the substring to the list of palindromes
            palindromes.append(sub_str)
    return set(palindromes)
