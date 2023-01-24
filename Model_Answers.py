# A python function that returns the list of all integers from x to y both inclusive.
def all_ints_inclusive(x,y):
    return [i for i in range(x, y+1) if x <= y]

# A python function that returns the list of all integers from x to y both exclusive.
def all_ints_exclusive(x,y):
    return [i for i in range(x+1, y) if x < y]

# A python function that returns the list of all positive integers from x to y both inclusive.
def all_pos_ints_inclusive(x,y):
    return [i for i in range(x, y+1) if x <= y and i > 0]

# A python function that returns the list of all positive integers from x to y both exclusive.
def all_pos_ints_exclusive(x,y):
    return [i for i in range(x+1, y) if x < y and i > 0]

# A python function that returns the list of all negative integers from x to y both inclusive.
def all_neg_ints_inclusive(x,y):
    return [i for i in range(x, y+1) if x <= y and i < 0]

# A python function that returns the list of all negative integers from x to y both exclusive.
def all_neg_ints_exclusive(x,y):
    return [i for i in range(x+1, y) if x < y and i < 0]

# A python function that returns the list of all even integers from x to y both inclusive.
def all_even_ints_inclusive(x,y):
    return [i for i in range(x, y+1) if x <= y and i%2==0]

# A python function that returns the list of all even integers from x to y both exclusive.
def all_even_ints_exclusive(x,y):
    return [i for i in range(x+1, y) if x < y and i%2==0]

# A python function that returns the list of all odd integers from x to y both inclusive.
def all_odd_ints_inclusive(x,y):
    return [i for i in range(x, y+1) if x <= y and i%2!=0]

# A python function that returns the list of all odd integers from x to y both exclusive.
def all_odd_ints_exclusive(x,y):
    return [i for i in range(x+1, y) if x < y and i%2!=0]

# A python function that returns the list of all integers from x to y that are divisible by n. Both x and y should be inclusive.
def all_ints_div_by_n_inclusive(x,y,n):
    return [i for i in range(x, y+1) if x <= y and i%n==0]

# A python function that returns the list of all integers from x to y that are divisible by n. Both x and y should be exclusive.
def all_ints_div_by_n_exclusive(x,y,n):
    return [i for i in range(x+1, y) if x < y and i%n==0]

# A python function that returns the list of all integers from x to y that are not divisible by n. Both x and y should be inclusive.
def all_ints_not_div_by_n_inclusive(x,y,n):
    return [i for i in range(x, y+1) if x <= y and i%n!=0]


# A python function that returns the list of all integers from x to y that are divisible by m and n. Both x and y should be inclusive.
def all_ints_div_by_m_n_inclusive(x,y,m,n):
    return [i for i in range(x, y+1) if x <= y and i%m==0 and i%n==0]

# A python function that returns the list of all integers from x to y that are divisible by m or by n. Both x and y should be inclusive.
def all_ints_div_by_m_n_inclusive(x,y,m,n):
    return [i for i in range(x, y+1) if x <= y and i%m==0 or i%n==0]

# A python function that returns the sum of all integers from x to y inclusive.
def sum_ints(x,y):
    return sum(range(x,y+1))

# A python function that returns the sum of all even integers from x to y inclusive.
def sum_even_ints(x,y):
    return sum([i for i in range(x,y+1) if i%2==0])

# A python function that returns the sum of all odd integers from x to y inclusive.
def sum_odd_ints(x,y):
    return sum([i for i in range(x,y+1) if i%2!=0])

# A python function that returns the sum of all integers from x to y that are divisible by n. Both x and y are inclusive.
def sum_ints_div_by_n(x,y,n):
    return sum([i for i in range(x,y+1) if i%n==0])



print(sum_ints_div_by_n(-10,10,7))  
print(sum_ints_div_by_n(-10,-10,7)) 
print(sum_ints_div_by_n(-10,1,7))   
print(sum_ints_div_by_n(0,10,11))    
print(sum_ints_div_by_n(0,1,1))     
print(sum_ints_div_by_n(10,10,10))   
print(sum_ints_div_by_n(10,20,11))