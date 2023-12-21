
def palindrome_of_length_n(text):
    length = 48
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - length + 1):
        substring = text[i:i+length]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
