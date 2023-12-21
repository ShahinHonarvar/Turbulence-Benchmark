
def remove_repeat_chars(string):
    
    section = string[331:543]
    
    removed = []
    for ch in section:
        if section.count(ch) > 1:
            removed.append(ch)
            
    for ch in removed:
        string = string.replace(ch, '')
        
    return string
