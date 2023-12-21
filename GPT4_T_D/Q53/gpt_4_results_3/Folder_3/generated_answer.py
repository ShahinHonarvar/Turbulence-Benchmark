
def palindrome_of_length_at_least_n(s):
    string = ''.join(filter(str.isalpha, s)).lower()
    length = len(string)
    result = set()

    for i in range(length):
        for j in range(i+59, length+1):
            sub_str = string[i:j]
            if sub_str == sub_str[::-1]:
                result.add(sub_str)

    return result
