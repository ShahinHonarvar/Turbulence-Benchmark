
def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)+1):
        for j in range(i):
            substring = string[j:i]
            if len(substring) >= 43 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
