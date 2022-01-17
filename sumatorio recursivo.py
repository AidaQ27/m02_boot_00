def sumatorio(n):
    if n > 0:
        return n + sumatorio(n-1)
    else:
        return 0
    
print(sumatorio(4))

# Hacer el mismo ejercicio pero factorial

def factorial(n):
    if n > 0:
        return n * factorial(n+1)
    else:
        return 0

print(factorial(12))