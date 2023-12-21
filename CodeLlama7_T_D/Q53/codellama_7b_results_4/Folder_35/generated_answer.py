 def palindrome_of_length_at_least_n(string, n):
    # Create a list of all substrings of the given string
    substrings = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.append(string[i:j])
    # Filter the substrings to find palindromes of length greater than or equal to n
    palindromes = []
    for substring in substrings:
        if len(substring) < n:
            continue

        if substring == substring[::-1]:
            palindromes.append(substring)
    return set(palindromes)
