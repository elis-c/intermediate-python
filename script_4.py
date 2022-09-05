sum = 0

for i in range(5):
    
    while True:
        try:
            x = int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter an integer. ")
            continue
        else:
            break
    sum = x+sum    

print(sum)
