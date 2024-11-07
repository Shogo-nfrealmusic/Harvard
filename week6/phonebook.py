# names = ['Michael', 'Bob', 'Tracy']

# name = input('Please enter your name: ')

# for n in names:
#     if name == n:
#         print("Found")
#         break
# else:
#     print("Not found")

# people = [
#  {"name": "Carter", "phone": "555-555-5555"},
#  {"name": "David", "phone": "111-111-1115"},
#  {"name": "John", "phone": "222-222-2225"},
# ]

people = {
    "Carter" : "555-555-5555",
    "David" : "111-111-1115",
    "John" : "222-222-2225" 
}


name = input("Name: ")

if name in people:
    number = people[name]
    print(f"Phone number: {number}")
else:
    print("Not found")

