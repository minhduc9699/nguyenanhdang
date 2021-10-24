numbers = [1, 6, 8, 1, 2, 1, 5, 6]

number_to_count = int(input('what number to count bro?: '))
count = 0
for number in numbers:
    if number == number_to_count:
        count = count + 1
print(count)

#dict 
number_count = {}
for number in numbers:
    if number in number_count:
        number_count[number] = number_count[number] + 1
    else:
        number_count[number] = 1
print(number_count[number_to_count])
