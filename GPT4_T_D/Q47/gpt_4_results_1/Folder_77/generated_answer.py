
def palindromes_of_specific_lengths(s):
    s = s[103:277]
    lst = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if j - i >= 100 and j - i <= 169:
                temp = s[i:j]
                if temp == temp[::-1] and temp.isalpha():
                    lst.append(temp.lower())
    return set(lst)
