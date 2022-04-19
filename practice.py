list = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]

for i in range(len(list)):
    result = 0
    first_level = list[i]
    print(f'printing elements from the first loop {first_level}')
    for j in range(len(first_level)):
        second_level = first_level[j]
        print(second_level)
        result += second_level
        print(result)

print('just for fun')

for item in list:
    total =0
    for subitem in item:
        total += subitem
    print(total)

print('new loop')
lst = [-2, 0, 4, 5, 1, 2]

result = 0

for item in lst:
    result += item
    print(result)

for i in range(len(lst)):
    result += lst[i]
    print(f'printing the totals of {result}')
