import csv

from collections import Counter

with open("week7/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = Counter()
    for row in reader:
        favorite = row["problem"]
        counts[favorite] += 1
        
favorite = input("Favorite: ")
print(f"{favorite}: {counts[favorite]}")
    # counts = {}
    # for row in reader:
    #     favorite = row["language"]
    #     if favorite in counts:
    #         counts[favorite] += 1
    #     else:
    #         counts[favorite] = 1

# for favorite , count in counts.most_common():
#     print(f"{favorite}: {count}")


#     scratch, c, python = 0, 0, 0
    
#     for row in reader:
#         favorite = row["language"]
#         if favorite == "Scratch":
#             scratch += 1
#         elif favorite == "C":
#             c += 1
#         elif favorite == "Python":
#             python += 1

# print(f"Scratch: {scratch}")
# print(f"C: {c}")
# print(f"Python: {python}")
    
    
