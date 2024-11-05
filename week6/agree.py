s = input("Do you agree? ")

s = s.lower()

# if s == "Y" or s == "y":
#     print("You agreed.")
# elif s == "N" or s == "n":
#     print("You disagreed.")

if s in ["y", "yes"]:
    print("You agreed.")
elif s in ["n", "no"]:
    print("You disagreed.")