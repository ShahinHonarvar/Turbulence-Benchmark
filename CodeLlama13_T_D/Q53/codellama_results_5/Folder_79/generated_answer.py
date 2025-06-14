
def palindrome_of_length_at_least_n(string, n):
    palindromes = set()
    for i in range(len(string) - n + 1):
        if string[i:i+n] == string[i+n-1:i-1:-1]:
            palindromes.add(string[i:i+n])
    return palindromes
