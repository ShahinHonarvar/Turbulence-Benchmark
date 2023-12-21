
def palindrome_of_length_at_least_n(string, n):
    # create a list of all the palindromes in the string
    palindromes = []
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if len(substring) < n:
            continue

        if substring == substring[::-1]:
            palindromes.append(substring)
    return set(palindromes)
