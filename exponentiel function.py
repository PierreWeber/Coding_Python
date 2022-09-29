num = (49**49)
print(num)

print(9**9)

def aug_vers_infini(num_base,inf_num):
    result = 1
    for index in range(inf_num):
        result = result * num_base
    return result

print(aug_vers_infini(2,3))