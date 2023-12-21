
def insert_before_character(s):
    result = ''
    for ch in s:
        if ch == 'O':
            result += 'j'
        result += ch
    return result
