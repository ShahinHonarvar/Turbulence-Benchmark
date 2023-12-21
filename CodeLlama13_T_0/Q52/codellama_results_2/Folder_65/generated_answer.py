
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 34):
        substring = string[i:i+35]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
