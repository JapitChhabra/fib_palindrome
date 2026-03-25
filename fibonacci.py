def fibonacci(n: int) -> list:
    """
    Generate a list of the first n Fibonacci numbers.

    Args:
        n (int): Number of terms

    Returns:
        list: Fibonacci sequence up to n terms
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0:
        return []
    elif n == 1:
        return [0]

    fib_seq = [0, 1]
    for _ in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq


if __name__ == "__main__":
    try:
        num = int(input("Enter the number of Fibonacci terms: "))
        result = fibonacci(num)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
