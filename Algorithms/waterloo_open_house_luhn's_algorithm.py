print("Please enter a number:")
number = input()

even_list = list()
odd_list = list()

for i in range(len(number)):
    if i % 2 == 1:
        even_list.append(number[i])
    elif i % 2 == 0:
        odd_list.append(number[i])

even_sum = 0
odd_sum = 0

for x in range(len(even_list)):
    even_sum = even_sum + int(even_list[x])

for a in range(len(odd_list)):
    if 2*int(odd_list[a]) > 9:
        odd_sum = odd_sum + (2*int(odd_list[a]) % 10)
        odd_sum = odd_sum + 1
    else:
        odd_sum = odd_sum + 2*int(odd_list[a])

total = even_sum + odd_sum

print(str(even_sum) + " + " + str(odd_sum) + " = " + str(total))

if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")
