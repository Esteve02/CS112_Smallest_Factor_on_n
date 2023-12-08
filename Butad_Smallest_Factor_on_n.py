def smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than or equal to 2.")
        return

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i

    return n  # If the number is prime, the smallest factor is the number itself


# Example usage:
num = int(input("Enter an integer greater than or equal to 2: "))
factor = smallest_factor(num)

if factor == num:
    print(f"{num} is a prime number.")
else:
    print(f"The smallest factor of {num} is {factor}.")

