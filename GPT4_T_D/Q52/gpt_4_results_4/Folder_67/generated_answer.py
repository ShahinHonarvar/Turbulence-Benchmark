
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()

    for i in range(len(s)):
        for j in range(i,len(s)):
            substr = s[i:j+1]
            if len(substr) == 42 and substr == substr[::-1] and substr.isalpha():
                result.add(substr)

    return result
