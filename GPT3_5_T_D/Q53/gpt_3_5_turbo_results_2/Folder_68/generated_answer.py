
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 20):
        substring = string[i:i+21]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
