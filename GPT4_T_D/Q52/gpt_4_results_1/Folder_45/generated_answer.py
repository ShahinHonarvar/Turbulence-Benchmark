
def palindrome_of_length_n(string):
    string = string.lower().replace(' ', '')
    result = set()
    for i in range(len(string)):
        for j in range(i + 21, len(string) + 1):
            substring = string[i:j]
            if ''.join(reversed(substring)).isalpha() and substring == ''.join(reversed(substring)):
                result.add(substring)
    return result
