
def palindrome_of_length_n(string):
    string = string.lower()
    only_letters = ''.join(ch for ch in string if ch.isalpha())
    length = 416
    palindromes = set()
    for i in range(len(only_letters) - length + 1):
        substring = only_letters[i:i+length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
