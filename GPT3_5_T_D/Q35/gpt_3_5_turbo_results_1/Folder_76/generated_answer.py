 
def remove_repeat_chars(string):
    return string[:330] + ''.join(c for c in string[330:543] if string[330:543].count(c) == 1) + string[543:]
