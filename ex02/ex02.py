def multiply_all(*args: int) -> int:
    prod = 1
    for n in args:
        prod *= n
    return prod
    pass

if __name__ == "__main__":
    
    print(multiply_all(1, 2, 3, 4, 5))
    print(multiply_all())
    print(multiply_all(7))