
import re

def return_nth_smallest_ascii(str):
    return next(i for i in range(ord("`")+20, ord("a")+1) if all(j < i for j in range(i+1, ord("a")+1)))
