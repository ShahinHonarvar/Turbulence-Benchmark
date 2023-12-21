
def palindrome_of_length_at_least_n(string):
    string = string.lower()
    set_palindromes = set()
    for i in range(len(string)):
        for j in range(i+14, len(string)+1):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                set_palindromes.add(substring)
    return set_palindromes
