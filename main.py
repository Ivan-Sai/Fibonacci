def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    print(n)
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

num = int(input("Введіть номер числа Фібоначчі: "))
result = [fibonacci_recursive(i) for i in range(num)]
print("Числа Фібоначчі:", result)
