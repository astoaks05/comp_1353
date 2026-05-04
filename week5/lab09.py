# MAD method
# Multiply, Add, Divide

N = 20
hashmap = {}
def hash(x):
    # return ((((13*x)+5)%23)%N)
    return (x%N)
vals = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
for num in vals:
    hash_val = hash(num)
    if hash_val not in hashmap:
        hashmap[hash_val] = [num]
    else: hashmap[hash_val].append(num)
print(hashmap)