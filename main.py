import math_operations as math_ops

def main():
    print("Willkommen beim Math-Tool!")
    
    ergebnis_plus = math_ops.add(10, 5)
    print(f"10 + 5 = {ergebnis_plus}")

    ergebnis_minus = math_ops.subtract(10, 5)
    print(f"10 - 5 = {ergebnis_minus}")

if __name__ == "__main__":
    main()