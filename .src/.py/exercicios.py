#1
def fatorial(n):
    if(n < 0):
        raise Exception('Menor que zero')
    if(n == 0 or n == 1):
        return 1
    return n * fatorial(n - 1)

#2
def somatorio(n):
    if(n == 0):
        return 0
    if(n > 0):
        return n + somatorio(n-1)
    if(n < 0):
        return n + somatorio(n+1)

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
def somatorioKJ(k, j):
    if (j < k):
        return somatorioKJ(j, k)
    if (j == k):
        return k
    return j + somatorioKJ(k, j - 1) 

#5
def palindrome(s):
    if(len(s) <= 1):
        return True
    if(s[0] != s[len(s)-1]):
        return False
    palindrome(s[1:-1])

#6
def convBase2(n):
    if (n < 1):
        return ''
    return str(n % 2) + str(convBase2(n / 2))

#7
def somatorioArray(list):
    if len(list) == 0:
        return 0
    list.pop() + somatorio(list)

#8
def maiorElemento(list):
    if(len(list) == 1):
        return list.pop()
    auxA = list.pop()
    auxB = maiorElemento(list)
    if(auxA >= auxB):
        return auxA
    else:
        return auxB
