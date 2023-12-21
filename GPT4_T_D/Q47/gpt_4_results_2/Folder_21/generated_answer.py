
def palindromes_of_specific_lengths(s):
    sub_s = s[100:296]
    pal_set = set()
    for i in range(len(sub_s)):
        for j in range(i + 136, i + 161):
            if j > len(sub_s):
                break
            temp = sub_s[i:j]
            if temp == temp[::-1] and temp.isalpha():
                pal_set.add(temp.lower())
    return pal_set
