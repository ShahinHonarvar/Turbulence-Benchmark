
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 471):
        substring = string[i:i+472].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
