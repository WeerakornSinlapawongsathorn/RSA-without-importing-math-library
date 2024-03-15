#!/usr/bin/env python3

import sys

#given e = 5 and n = 10142789312725007 public key
#encrypt m = 256
#finding d and privare-key for encryption
#equations: ed = 1mod(t_n)
#equations: private (c) = (m^d)mod n & public (p) = (c^e)mod n
def rsa(e,n):
    #n = p*q
    p, q = multi_prime(n)
    if q == 1:
        t_n = (n-1)
    else:
        t_n = (p-1) * (q-1)
    d = multi_inverse(e,t_n)
    c = encryption(256,d,n)
    print(d,c) 

#finding c first
#because c has m^e and m = 256
#high value of the power
#exponential
#(a*b*c)mod m = (((a*b)mod m)*c)mod m
#(123^54)mod675 = (123 * 123)mod678
    #123^2 = 123 * 123 mod 678 = 213
    #123^4 = 213 * 213 mod 678 = 621
    #123^8 = 621 * 621 mod 678 = 537
    #123^12 = 621 * 537 mod 678 = 579 
    #123^22 = 213 * 621 * 537 * 579 mod 678 = 51
    #123^44 = 51*51 mod 678 = 567
    #123^54 = 567 * 213 * 537 mod 678 = 615
#first time I do not have message = (message*message)%n1
    #the output is larger than the desired number output.
    #Because always multiply resulting fastly growing number
#Reference: Youtube: the fast modular exponentialtion algorithm in python by JacksonInfoSec 
def encryption(message, e1 ,n1):
    result = 1
    #for i in range(e1): no output
    while e1 > 0:
        if e1 % 2 == 1:
            #123^1 = 123*1 mod678 = 123
            #123^3 = 123*213 mod678
            result = (result * message) % n1 
        #123^2 = (123*123) mod 678 = 213
        message = (message*message) % n1
        #e1 -= 1 first negative output and then, no output
        e1 = e1 // 2
    return result 

#finding d = (modulo(t_n)+1)/e
#find t_n from given n 
#n = prime * prime
#if n is already prime, t_n = n-1
def multi_prime(n):
    p = 2 
    while p <= n:
        if n % p == 0:
            q = n // p #the factors are the multiple of two numbers, if n = p*q, q = n/p
            #check if p and q are prime
            if is_prime(p) and is_prime(q):
                return p,q
        p += 1
    #The first time, I return n, 2 to prevent q = 1 and t_n = 0
    #But I have tried with Jupyter Notebook, when n = 17, it returns p = 17 and q = 2, I decided to return n, 1 because of confusion prevention.
    return n, 1

#check prime

def is_prime(prime):
    if prime < 2:
        return False
    #for i in range(2, prime+1): --> no output
    #reference from Youtube: Efficient Prime Numbers in Python by Neal Holtschulte
    for i in range(2, int(prime // 2)+1):
        if prime % i == 0:
            return False
    return True


#Now already coded for t_n, p, q and c. 
#d left
# d = ((t_n*n)+1)/e
#Because I have tried to directly return value from extended_Euc, the output was 0 1
#I am confused because it is possible that T1 = negative
#I just know about the strange of modular of python, such as if (-2)%7 = 5 not -2 in python
#I tried to use result1%number, and it works, but if I directly returned from the extended_Euc, I am confused since b value is from the while loop.
def multi_inverse(e2, number):
    result1 = extended_Euc(e2,number)
    #return result1 --> output of the code is negative
    return result1 % number    

#Reference: Neso Academy Youtube: Extended Euclidean Algorithm
def extended_Euc(a,b):
    T1,T2 = 0, 1
    #b = t_n and a = e
    while a != 0:
        # a = b%a and b = a  
        q = b // a 
        r = b % a 
        b = a
        a = r 
        T = T1 - T2*q 
        T1 = T2
        T2 = T 
    return T1

#def gcd(a, b):
#while b != 0:
        #a = b
        #b = a % b
    #return a


e = int(sys.argv[1])
n = int(sys.argv[2])
rsa(e,n)

    





