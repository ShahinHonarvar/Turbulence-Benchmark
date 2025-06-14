
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 59 + 1):
        substring = string[i:i+59]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
