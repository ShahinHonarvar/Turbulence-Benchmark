
def palindrome_of_length_at_least_n(string):
    string = string.lower()
    result = set()
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring= string[i: j + 1]
            if len(substring) >= 150 and substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result
