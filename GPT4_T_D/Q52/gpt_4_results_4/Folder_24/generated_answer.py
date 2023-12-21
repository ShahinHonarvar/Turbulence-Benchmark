
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()

    for i in range(0, len(string)):
        for j in range(i+29, len(string)+1):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
            
    return palindromes
