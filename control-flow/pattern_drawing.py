row = int(input("Enter the size of the pattern:"))
current_row = 0
while current_row < row:
    
    for col in range(row):
            print("*", end=" ")
    print()
    current_row += 1
    