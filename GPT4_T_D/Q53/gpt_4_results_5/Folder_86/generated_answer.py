
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()  # preserve only alphabetical characters
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 133, length+1):
            sub = s[i:j]
            if sub == sub[::-1]:  # check if it's a palindrome
                result.add(sub)
    return result
