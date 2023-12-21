
def palindrome_of_length_n(string):
    string = string.lower()
    result = set()
    for i in range(len(string)):
        for j in range(i+85, len(string)+1):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result
