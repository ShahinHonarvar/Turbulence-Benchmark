
def remove_repeat_chars(s):
    to_remove = [] 
    for char in set(s[41:200]):  
        if s[41:200].count(char) > 1:  
            to_remove.append(char) 
    for char in to_remove:  
        s = s.replace(char, '')  
    return s
