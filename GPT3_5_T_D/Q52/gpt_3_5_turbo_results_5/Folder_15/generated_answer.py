
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 3):
        if string[i:i+4] == string[i:i+4][::-1] and string[i:i+4].isalpha():
            palindromes.add(string[i:i+4])
    return palindromes
