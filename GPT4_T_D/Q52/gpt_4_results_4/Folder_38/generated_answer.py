
def palindrome_of_length_n(string):
    string = string.lower()
    res = set()
    for i in range(len(string)-37):
        check_string = string[i:i+38]
        if all(c.isalpha() for c in check_string) and check_string == check_string[::-1]:
            res.add(check_string)
    return res
