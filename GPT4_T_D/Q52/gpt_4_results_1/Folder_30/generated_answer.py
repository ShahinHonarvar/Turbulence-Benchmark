
def palindrome_of_length_n(string):
    res = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i+94, len(string)+1):
            if j-i == 94:
                substring = string[i:j]
                if substring == substring[::-1] and substring.isalpha():
                    res.add(substring)
    return res
