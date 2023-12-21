
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the string
    palindromes = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.append(substr)
    # Filter the palindromes to only include those with lengths between 10 and 20 (both inclusive)
    filtered_palindromes = []
    for palindrome in palindromes:
        if len(palindrome) >= 10 and len(palindrome) <= 20:
            filtered_palindromes.append(palindrome)
    # Return the set of filtered palindromes
    return set(filtered_palindromes)
