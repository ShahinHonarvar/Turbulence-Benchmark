
def palindrome_of_length_n(string):
    n = 445
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - n + 1):
        if string[i:i+n] == string[i:i+n][::-1] and string[i:i+n].isalpha():
            palindromes.add(string[i:i+n])
    return palindromes
