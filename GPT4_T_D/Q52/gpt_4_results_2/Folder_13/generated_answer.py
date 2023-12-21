
def palindrome_of_length_n(string):
    string = string.lower()
    result = set()
    length = 206
    for i in range(0, len(string) - length + 1):
        substring = string[i:i+length]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result
