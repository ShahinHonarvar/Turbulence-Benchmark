
def palindrome_of_length_n(inp_str):
    inp_str = inp_str.lower()
    len_str = len(inp_str)
    palindromes = set()
    for i in range(len_str):
        for j in range(i+35, len_str+1):
            substring = inp_str[i:j]
            if len(substring) == 35 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
