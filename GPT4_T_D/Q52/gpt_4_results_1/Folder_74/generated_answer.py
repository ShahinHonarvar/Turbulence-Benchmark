
def palindrome_of_length_n(st):
    n = 96
    st = st.lower()
    res = set()
    
    for i in range(len(st)):
        for j in range(i+n, len(st)+1):
            substring = st[i:j]
            if substring == substring[::-1]:
                if substring.isalpha():
                    res.add(substring)
    return res
