
def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 111):
        for j in range(i+111, len(string)):
            substring = string[i:j+1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
