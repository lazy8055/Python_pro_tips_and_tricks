# check multiples conditions that all conditions are need to be true:

ice_cream = True
flavor = 10
best = "Butterscotch"
price = 200

# Worst to pro method to check that all condition are true

# 1. Check using nested if condition:

print("\n[*] Check using nested if condition:")
if ice_cream:
    if flavor > 5:
        if best == "Butterscotch":
            if price < 500:
                print("All conditions are true!")
            else:
                print("Not all conditions are true!")
        else:
            print("Not all conditions are true!")
    else:
        print("Not all conditions are true!")
else:
    print("Not all conditions are true!")

# 2. Using and keyword:

print("\n[*] Check using and keyword:")
if ice_cream and flavor > 5 and best == "Butterscotch" and price < 500:
    print("All conditions are true!")
else:
    print("Not all conditions are true!")

# 3. Using a list and all() function:

print("\n[*] Check using a list and all() function:")
conditions = [ice_cream, flavor > 5, best == "Butterscotch", price < 500]
if all(conditions):
    print("All conditions are true!")
else:
    print("Not all conditions are true!")