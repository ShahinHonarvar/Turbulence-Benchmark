
def remove_repeat_chars(s):
    start = 50
    end = 200
    if len(s) < end:
        end = len(s)
    
    string_between_indices = s[start + 1:end]
    repeat_chars = [char for char in string_between_indices if string_between_indices.count(char) > 1]
    
    result = ''
    for i in s:
        if i not in repeat_chars:
            result += i
            
    return result
