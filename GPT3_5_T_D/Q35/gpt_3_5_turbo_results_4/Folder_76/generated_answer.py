
def remove_repeat_chars(string):
    return string[:330] + ''.join([c for i, c in enumerate(string[330:543]) if c not in string[330:543][i+1:543]]) + string[543:]
