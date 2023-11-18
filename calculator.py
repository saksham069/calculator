def addition(n1, n2):
    return n1 + n2

def main():
    num1 = int(input("first nunber: "))
    num2 = int(input("second nunber: "))
    op = input("operation to perform: ")

    if op == '+':
        print(addition(num1, num2))
    else:
        print("Invalid!")


if __name__ == "__main__":
    main()