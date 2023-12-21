
def palindrome_of_length_n(string):
    length = 210
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
