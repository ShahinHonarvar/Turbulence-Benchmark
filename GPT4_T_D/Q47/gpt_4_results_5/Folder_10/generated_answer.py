
def palindromes_of_specific_lengths(s):
    string = s[16:61]
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+16, min(i+40, len(string)+1)):
            substring = string[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes
