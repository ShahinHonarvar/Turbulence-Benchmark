
def palindrome_of_length_n(string):
    string = string.lower()
    string = ''.join(e for e in string if e.isalnum()) 
    palindromes = set()
    for i in range(len(string)-36):
        substring = string[i:i+37]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
