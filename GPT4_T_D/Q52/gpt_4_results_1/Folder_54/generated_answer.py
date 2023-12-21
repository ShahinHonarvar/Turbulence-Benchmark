
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 84):
        substring = string[i:i+85]
        if not substring.isalpha():
            continue
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
