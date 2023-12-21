
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string)):
        substring = string[i:]
        if len(substring) < 51:
            continue
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
