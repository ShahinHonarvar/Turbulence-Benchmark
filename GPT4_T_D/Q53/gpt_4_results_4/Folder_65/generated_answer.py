
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    result_set = set()
    length = len(s)
    for i in range(length):
        for j in range(i+15, length+1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result_set.add(substring)
    return result_set
