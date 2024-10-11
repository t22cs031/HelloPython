'''
2024/10/11
@uta

フィボナッチ数列
'''

def fibo(n):
    if n==0 or n==1:
        return 1
    return fibo(n-1) + fibo(n-2)