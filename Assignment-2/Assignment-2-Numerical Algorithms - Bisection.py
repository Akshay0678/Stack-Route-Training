# Assignment - 2 - Algorithmic coding assignment
# Algorithm - Implement Bisection/Binary Search in Python
# Created on Fri Mar 24 09:22:09 2017

# @author: Akshay Tomar (AK357172)


function = input("Enter the function(parameter should be 'x') : ")
a_val = float(input("Enter the starting value(a): "))
b_val = float(input("Enter the starting value(b): "))
tolerance = float(input("Enter the tolerance value: "))
max_iter = int(input("Enter maximum number of iterations: "))


def bi_section(func, a, b, tol, m_iter):
    x = a
    f_a = eval(func)
    x = b
    f_b = eval(func)
    if (sign(f_a) == sign(f_b)):
        print ("Error: Enter proper values of a and b")
        return
    cnt = 0
    for cnt in range(m_iter):
        x = a
        f_a = eval(func)
        c = float((a + b))/2
        x = c
        f_c = eval(func)
        if ((f_c == 0) | ((b - a)/2 < tol)):
            print ("Root found = ", c)
            return
        if ((f_c * f_a) > 0):
            a = c
        else:
            b = c
    print ("Method Failed_xoxo - Root not found")
    return

bi_section(function, a_val, b_val, tolerance, max_iter)

