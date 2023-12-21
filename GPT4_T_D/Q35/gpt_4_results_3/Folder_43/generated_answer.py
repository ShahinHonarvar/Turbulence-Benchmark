
def remove_repeat_chars(s):
    repeat_chars= [char for char in s[11:28] if s[11:28].count(char)>1]
    
    result=[]
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)
