 
def remove_repeat_chars(s):
    remove_chars = set()
    for i in range(462, 995):
        char = s[i]
        if char in s[462:i] or char in s[i+1:995]:
            remove_chars.add(char)
    return ''.join([c for c in s if c not in remove_chars])
