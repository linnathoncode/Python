def even_or_odd():
    numb = int(input("Enter your number: "))
    if numb % 2 == 0:
        print(f"{numb} is an even number")
    else:
        print(f"{numb} is an odd number")

if __name__ == "__main__":
    even_or_odd()