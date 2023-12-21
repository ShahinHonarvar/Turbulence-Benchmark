
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 12):
        substring = string[i:i+13]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
