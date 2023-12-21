
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the substring
    palindromes = []
    for i in range(16, 61):
        for j in range(i + 1):
            substr = string[j:i]
            if substr == substr[::-1]:
                palindromes.append(substr)
    # Filter the palindromes by length and case sensitivity
    filtered_palindromes = []
    for palindrome in palindromes:
        if len(palindrome) in range(16, 40) and all(c.isalpha() for c in palindrome):
            filtered_palindromes.append(palindrome)
    return set(filtered_palindromes)
