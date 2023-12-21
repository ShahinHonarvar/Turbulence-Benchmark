
def palindrome_of_length_n(string):
    set_of_palindromes = set()
    length = 210
    string = string.lower()
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if substring == substring[::-1] and substring.isalpha():
            set_of_palindromes.add(substring)
    return set_of_palindromes
