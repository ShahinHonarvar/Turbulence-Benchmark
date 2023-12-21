
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub('[^A-Za-z]', '', s).lower()
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 35, length + 1):
            temp = s[i:j]
            if temp == temp[::-1]:
                result.add(temp)
    return result
