
def return_binary_or_hexa(nums):
    # Integers a and b from the tuple
    a = nums[275]
    b = nums[871]

    # Calculate the sum of missing integers in the tuple from a+1 to b-1
    missing_sum = sum(set(range(a+1, b)) - set(nums[275:872]))
    
    # Return the binary or hexadecimal representation of the computed sum
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:] 
    else:
        return bin(missing_sum)[2:] if missing_sum != 0 else ""
