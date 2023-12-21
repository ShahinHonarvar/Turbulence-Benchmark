
def palindrome_of_length_n(string):
    palindromes = set()
    length = 84

    for i in range(len(string) - length + 1):
        substring = string[i:i+length].lower()
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
