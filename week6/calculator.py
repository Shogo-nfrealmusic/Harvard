def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input, please try again")
        return get_int(prompt)

def main():
    x = get_int("x: ")
    y = get_int("y: ")
    
    print(x + y)
    
main()