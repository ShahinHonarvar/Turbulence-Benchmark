
def palindrome_of_length_n(string):
    len_n_palindromes = set()
    string = string.lower()
    for i in range(len(string) - 63):
        substring = string[i:i+64]
        if substring.isalpha() and substring == substring[::-1]:
            len_n_palindromes.add(substring)
    return len_n_palindromes
