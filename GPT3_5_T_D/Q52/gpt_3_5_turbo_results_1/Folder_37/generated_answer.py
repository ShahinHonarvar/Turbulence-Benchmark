
def palindrome_of_length_n(s):
    palindromes = []
    length = 84
    for i in range(len(s) - length + 1):
        substring = s[i:i+length]
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.append(substring)
    return set(palindromes)
