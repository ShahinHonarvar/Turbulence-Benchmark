
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i+43, len(s)+1):
            temp = s[i:j]
            if temp == temp[::-1]:
                result.add(temp)
    return {x for x in result if x.isalpha()}
