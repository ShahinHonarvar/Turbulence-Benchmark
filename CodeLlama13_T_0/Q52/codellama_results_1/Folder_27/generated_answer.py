
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 56 + 1):
        substring = string[i:i+56]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
