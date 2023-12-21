
def palindrome_of_length_n(string, n):
    if n <= 0:
        return set()
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
