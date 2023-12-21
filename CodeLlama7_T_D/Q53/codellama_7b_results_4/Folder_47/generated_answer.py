
def palindrome_of_length_at_least_n(string, n):
    # Create a list of all palindromes in the string
    palindromes = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if len(substring) < n:
                continue

            if substring == substring[::-1]:
                palindromes.append(substring)
    return set(palindromes)
