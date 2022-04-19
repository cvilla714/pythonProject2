def replace(list,target,swap_value):
    for i in range(len(list)):
        if list[i] == target:
            list[i] = swap_value
    return list

print(replace([1,2,3,4,5,3,7,3],3,0))
print(replace(["time","flies","like","an","arrow","like","it","is","too","like"],"like","love"))
print(replace(["time","hello","great"],"hello","is"))