# Returns the nth Fibonacci number
def fib(n):
    if n == 1:
        return 0
    else:
        return fib(n-1) + fib(n-2)
