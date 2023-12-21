
def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i + 6, length + 1):
            sub_string = string[i:j]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                palindromes.add(sub_string)
    return palindromes
