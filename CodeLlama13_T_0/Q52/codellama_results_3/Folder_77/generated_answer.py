
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 172):
        substring = string[i:i+173]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
