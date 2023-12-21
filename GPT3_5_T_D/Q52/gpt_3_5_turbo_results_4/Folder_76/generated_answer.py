
def palindrome_of_length_n(string):
    n = 257
    palindromes = set()
    string = string.lower()
    for i in range(len(string)-n+1):
        substring = string[i:i+n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
