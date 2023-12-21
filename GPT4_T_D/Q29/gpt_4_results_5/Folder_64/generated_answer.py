
import math

def gcf_two_nums(arr):
    if len(arr) < 10:
        return "List must contain at least 10 elements."
    else:
        return math.gcd(arr[6], arr[9])
