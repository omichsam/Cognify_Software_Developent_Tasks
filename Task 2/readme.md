# Pyramid Number Pattern Generator 🧱

This Python program generates a simple number pattern in the form of a pyramid. It's a basic exercise in using nested loops to control output formatting, ideal for beginners learning Python programming and control flow structures.

---

## 📌 Objective

To utilize loops (especially nested loops) to generate and control the structure of a number pyramid pattern.

---

## 🧩 Pattern Description

Given an integer input `n`, the program prints a pyramid of numbers where each row contains an increasing sequence from `1` to the row number, right-aligned to form a pyramid shape.

### ✅ Example Output (n = 5)
```
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
```

---

## 🛠️ How It Works

1. The user is prompted to enter the number of rows.
2. The outer loop iterates through each row.
3. The first inner section adds spaces to align the numbers as a pyramid.
4. The second inner loop prints the numbers from `1` to the current row number.

---

## 📦 Usage

### 🔁 Run in terminal:
```bash
python pyramid_pattern.py
```

### Code
```
# pyramid_pattern.py

# Ask user for number of rows
rows = int(input("Enter the number of rows: "))

# Generate the pyramid pattern using loops
for i in range(1, rows + 1):
    # Print leading spaces
    print(" " * (rows - i), end="")

    # Print the numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Move to the next line
    print()
```

### 🚀 Author
Your Name : Samson Michira

GitHub: <a href="https://github.com/omichsam"><b>omichsam</b></a>