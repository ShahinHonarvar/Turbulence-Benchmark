
import binary
import hexadecimal

def return_binary_or_hexa(tup):
    for i in range(len(tup)):
        if tup[i] <= 13: continue
        if tup[i] <= 70: continue
        else:
            if binary.check_odd(tup[13]+1, tup[70]-1):
                return binary.to_binary(tup[13]+1, tup[70]-1)
            else:
                return hexadecimal.to_hexadecimal(tup[13]+1, tup[70]-1)
    return ""
