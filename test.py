'''
def tribonacci(signature, n):
    next_number = 0

    new_signature = signature
    for i in signature:
        checker = signature.index(i) % 4
        if checker == 0 and i != 0:
            next_number += i
        elif checker == 1 or checker == 2:
            next_number += i
        elif checker == 3:
            new_signature.append(next_number)
            next_number = 0
    return new_signature
'''

def tribonacci(signature, n):   # n = desired length
    while len(signature) < n:
        next_number = signature[-3] + signature[-2] + signature[-1]
        signature.append(next_number)
    return signature


    # new_signature = signature
    # for i in range(n):
    #     next_number = new_signature[-3:]
    #     new_signature = new_signature.append(next_number)
    # return new_signature


new_array = [0,1,1,2,4,7,14]
print([new_array[0]])


#print(tribonacci([0,1,1,2,4,7,14], 10))