
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        substring = string[i:i+84]
        if len(substring) == 84 and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
