
def palindrome_of_length_at_least_n(string, n):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            if len(substring) >= n and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
