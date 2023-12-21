
def palindrome_of_length_n(text_string):
    text_string = text_string.lower()
    palindromes = set()
    for i in range(len(text_string) - 16):
        substring = text_string[i:i+17]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
