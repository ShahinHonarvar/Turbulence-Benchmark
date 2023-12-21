
def palindrome_of_length_n(string):
    length = 53
    palindromes = set()
    for i in range(len(string)):
        if len(string[i:]) < length: continue
        substring = string[i:i+length]
        if not all([x.isalpha() for x in substring]): continue
        if substring == substring[::-1]: palindromes.add(substring)
    return palindromes
