# Printing a list containing strings
name = ['first', 'second', 'third', 'fourth', 'fifth']

# Worst to pro method to print a list

# 1. print one by one:
print("\n[*] Printing one by one:")
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# 2. Using a loop:
print("\n[*] Using a loop:")
for i in name:
    print(i)

# 3. Using join() function:
print("\n[*] Using join() function:")
print("\n".join(name))