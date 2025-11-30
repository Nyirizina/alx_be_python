import sys
# Importing the function from the file created above
from robust_division_calculator import safe_divide

def main():
    # check if the list of arguments contains exactly 3 elements
    # (The script name + numerator + denominator)
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the imported function
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()