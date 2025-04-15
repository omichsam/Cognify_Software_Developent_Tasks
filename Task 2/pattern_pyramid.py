# Step 1: Ask user for the number of rows
rows = int(input("Enter the number of rows: "))

# Step 2 & 3: Generate the pyramid pattern using loops
for i in range(1, rows + 1):
    # Print spaces for alignment
    print(" " * (rows - i), end="")
    
    # Print the numbers in each row2
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Move to the next line
    print()
