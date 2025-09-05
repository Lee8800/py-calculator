def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def divide(a: float, b: float) -> float:
    if b  == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def multiply(a: float, b: float) -> float:
    return a * b    

if __name__ == "__main__":
    print("Simple Calculator")
    while True:
        try:
            op = input("Choose operation (+, -, *, /) or q to quit: ").strip().lower()
            if op == "q":
                break
            if op not in {"+", "-", "*", "/"}:
                print("Invalid operation. Try +, -, * or /.")
                continue
            a = float(input("First number: "))
            b = float(input("Second number: "))

            if op == "+":
                result = add(a, b) 
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            else:
                result = divide(a, b)
                
            print(f"Result: {result}\n")
        except ValueError:
            print("Please enter valid numbers.\n")
