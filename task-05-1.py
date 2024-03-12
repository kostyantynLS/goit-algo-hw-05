'''
Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання і 
повторного використання вже обчислених значень чисел Фібоначчі.

Вимоги до завдання:
- Функція caching_fibonacci() повинна повертати внутрішню функцію fibonacci(n).
- fibonacci(n) обчислює n-те число Фібоначчі. Якщо число вже знаходиться у кеші, функція має повертати значення з кешу.
- Якщо число не знаходиться у кеші, функція має обчислити його, зберегти у кеш та повернути результат.
- Використання рекурсії для обчислення чисел Фібоначчі.
'''

"""Generate Fibonacci numbers using an internal function to store values."""
def caching_fibonacci():
    # Initialize the cache with the first two Fibonacci numbers
    cache = [0, 1]
    
    def fibonacci(n):
        # check cache
        nonlocal cache
        if n <= 0:
            return cache[0]
        if n == 1:
            return cache[1]
        if n < len(cache):
            return cache[n]
        if n == len(cache):
            # Generate and cache the next Fibonacci number
            cache.append(cache[-2] + cache[- 1])
            return cache[len(cache) - 1]
        # recursive calls
        if n > len(cache):
            return fibonacci(n-2)+fibonacci(n-1)
        
    return fibonacci

'''
fib = caching_fibonacci()
print(fib(10))
print(fib(2))
print(fib(5))
'''
