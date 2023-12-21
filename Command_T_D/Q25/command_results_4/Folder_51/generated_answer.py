
import re

def insert_at_index(a):
    i = len(a)
    j = i + 1
    a[i:j] = re.sub(r"(\d+\.,){2}\d+)", r"\1 249.61\3", a[i:j])
    return a[:i] + a[j:]
