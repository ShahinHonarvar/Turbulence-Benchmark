import re
import sys

def instantiate(template, args):

    return re.sub(r'\$', lambda i: str(args.pop(0)), template)

template = open(sys.argv[1], "r").read()

print(instantiate(template, sys.argv[2:]))
