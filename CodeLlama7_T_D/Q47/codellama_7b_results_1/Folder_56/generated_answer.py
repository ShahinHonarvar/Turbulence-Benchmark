
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the given string
    palindromes = []
    for i in range(1, len(string) - 8):
        for j in range(i + 1, len(string) - 7):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.append(substr)
    # Filter out palindromes of invalid lengths
    filtered_palindromes = []
    for palindrome in palindromes:
        if len(palindrome) >= 3 and len(palindrome) <= 7:
            filtered_palindromes.append(palindrome)
    return filtered_palindromes
