
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    lst = []
    for char in s[260:322]:
        if char > '%' and char <= 'U' and char in vowels:
            lst.append(char)
    return lst
