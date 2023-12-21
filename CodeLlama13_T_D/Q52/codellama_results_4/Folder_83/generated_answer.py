
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i, len(string)-23):
            substring = string[i:j+24]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
