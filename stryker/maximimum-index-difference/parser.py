import fileinput

n = 0
list_a = []
list_b = []
index_diffs = {}
counter = 1
for line in fileinput.input():
    if counter == 1:
        n = line
    elif counter == 2:
        list_a = line.split()
    elif counter == 3:
        list_b = line.split()
    counter += 1

i = 0
while (i < len(list_a)):
    num = list_a[i]
    index_in_list_a = i
    index_in_list_b = list_b.index(num)
    index_diffs[num] = abs(index_in_list_a - index_in_list_b)
    i += 1
    
min_index = -1
min_diff = -1
for k, v in index_diffs.items():
    if int(min_index) < 0:
        min_index = int(k)
        min_diff = int(v)
    elif (int(v) < min_diff) or ((int(v) == min_diff) and (int(k) < min_index)):
          min_index = int(k)
          min_diff = int(v)

print(min_index)