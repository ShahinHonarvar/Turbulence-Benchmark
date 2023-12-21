
def palindromes_of_specific_lengths(string):
    import re
    string = string[75:96].lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+7, min(i+10, len(string)+1)):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
