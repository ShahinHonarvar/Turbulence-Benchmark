import sys

def instantiate(template, args):
    result = ""
    args_index = 0
    for i in range(0, len(template)):
        if template[i] == "$":
            result += args[args_index]
            args_index += 1
        else:
            result += template[i]
    return result

template = open(sys.argv[1], "r").read()

print(instantiate(template, sys.argv[2:]))
