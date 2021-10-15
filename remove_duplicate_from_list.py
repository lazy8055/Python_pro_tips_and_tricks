# Remove the duplicates from a list
num = [10, 30, 10, 40, 40, 20, 10, 30, 60 ,100]

#Worst to pro method to remove duplicates from the list

# Check one by one using loop:
print("\n[*] Check one by one using loop:")
num2 = []
for i in num:
    if i not in num2:
        num2.append(i)
print(num2)

# Using list comprehension:
print("\n[*] Using list comprehension:")
num2 = []
[num2.append(x) for x in num if x not in num2]
print(num2)

# Using set:
print("\n[*] Using set:")
num2 = []
num2 = list(set(num))
print(num2)