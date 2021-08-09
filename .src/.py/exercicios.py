#1
def fatorial(n):
    if(n < 0):
        raise Exception('Menor que zero')
    if(n == 0 or n == 1):
        return 1
    return n * fatorial(n - 1)

#2
def somatorio(n):
    if(n < 0):
        raise Exception('Menor que zero')
    if(n == 0):
        return 0
    return n + somatorio(n- 1)

#3
def fibonacci(n):
    if(n < 1):
        raise Exception('Menor que um')
    if(n == 1):
        return 0
    if(n == 2):
        return 1
    return fibonacci(n -1) + fibonacci(n -2)

#4
def somatoioKJ(k, j):
    if (j < k)
        raise Exception('Somatório exedeu limite inferior')
    if (j = k)
        return k
    return j + somatorioKJ(k, j - 1)