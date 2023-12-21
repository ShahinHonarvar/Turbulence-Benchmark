
import sys

input = sys.stdin.readline

def insert_at_index(arr):
    res = []
    for i in range(len(arr)):
        if arr[i] == "581.49":
            res.append("581.49")
            break
        else:
            res.append(arr[i])
    return res + [0]
