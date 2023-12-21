
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)-2):
        sub_string = string[i:i+3]
        if sub_string == sub_string[::-1] and sub_string.isalpha():
            palindromes.add(sub_string)
    return palindromes
