sheeps = [55, 57, 350, 140, 74, 125]


total = sum(sheeps)

total_plus = 0
for x in sheeps:
    total_plus = total_plus + x
print(total_plus, total)
sheeps_plus = [x + 50 for x in sheeps]

new_list = []
for x in sheeps:
    new_list.append(x + 50)
# print(sheeps_plus)
# print(new_list)