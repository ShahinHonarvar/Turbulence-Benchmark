
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    
    for i in range(len(s) - 65):
        temp = s[i : i + 66]
        if temp == temp[::-1] and temp.isalpha():
            result.add(temp)
    
    return result
