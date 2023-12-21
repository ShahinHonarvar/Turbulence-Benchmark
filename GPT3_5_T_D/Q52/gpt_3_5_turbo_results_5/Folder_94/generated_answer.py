
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    length = 93
    for i in range(len(string) - length + 1):
        if string[i:i+length] == string[i:i+length][::-1] and string[i:i+length].isalpha():
            palindromes.add(string[i:i+length])
    return palindromes
