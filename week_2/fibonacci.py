def print_fibonacci(n):
    # Initialize the first two terms of the Fibonacci sequence
    a, b = 0, 1
    count = 0

    while count < n:
        print(a, end=' ')
        # Update the terms
        a, b = b, a + b
        # Increment the count
        count += 1


number = int(input("Enter the number of terms for the Fibonacci sequence: "))
if number <= 0:
        print("Please enter a positive integer.")
else:
        print("Fibonacci sequence:")
        print_fibonacci(number)

