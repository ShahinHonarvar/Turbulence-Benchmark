
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 473):
        substring = string[i:i+474]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
