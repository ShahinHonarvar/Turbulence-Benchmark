import re
def return_n_greatest_chars(str_arg):
    str_arg = re.sub(r'\W+', '', str_arg)
    str_arg = str_arg.split('')
    str_arg = sorted(str_arg, key=lambda x: ord(x))
    str_arg = str_arg[:20]
    str_arg.sort(reverse=True)
    return str_arg
