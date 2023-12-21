
def palindrome_of_length_at_least_n(string):
    n = 137
    palindromes = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j + 1]
            if len(substring) >= n and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
