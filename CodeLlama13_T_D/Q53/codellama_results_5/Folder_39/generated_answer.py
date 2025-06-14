
def palindrome_of_length_at_least_n(string, n):
    palindromes = set()
    for i in range(len(string)):
        if len(string[i:]) < n:
            continue
        for j in range(len(string), 0, -1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
