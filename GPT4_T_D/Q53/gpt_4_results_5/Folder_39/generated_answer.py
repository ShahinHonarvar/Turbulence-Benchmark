
def palindrome_of_length_at_least_n(string):
    import re
    string = string.lower()
    string = re.sub('[^a-z]', '', string)
    length = len(string)
    palindromes = set()
    for i in range(length):
        for j in range(i + 69, length + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
