
def palindrome_of_length_n(input_string):
    res = set()
    stripped_string = ''.join(e for e in input_string if e.isalnum()).lower()
    for i in range(len(stripped_string)): 
        for j in range(i, len(stripped_string)): 
            temp_str = stripped_string[i: j + 1] 
            if len(temp_str) == 49:
                if temp_str == temp_str[::-1]: 
                    res.add(temp_str)
    return res
