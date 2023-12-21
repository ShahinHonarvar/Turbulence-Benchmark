
def palindrome_of_length_n(s):
    s = s.lower()
    all_palindromes = set()
    for i in range(len(s) - 36):
        substring = s[i:i+37]
        if all(char.isalpha() for char in substring) and substring == substring[::-1]:
            all_palindromes.add(substring)
    return all_palindromes
