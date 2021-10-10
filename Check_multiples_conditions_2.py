# check multiples conditions that any conditions is true:

ice_cream = False
flavor = 10
best = "Butterscotch"
price = 200

# Worst to pro method to check that any condition is true


# 1. Using or keyword:

print("\n[*] Check using or keyword:")
if ice_cream or flavor > 5 or best == "Butterscotch" or price < 500:
    print("All Conditions may true!")
else:
    print("Conditions are False!")

# 2. Using a list and any() function:

print("\n[*] Check using a list and all() function:")
conditions = [ice_cream, flavor > 5, best == "Butterscotch", price < 500]
if any(conditions):
    print("All Conditions may true!")
else:
    print("Conditions are False!")