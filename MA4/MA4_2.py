#!/usr/bin/env python3

from person import Person
from fibonacci import fib_py, fib_numba
import time


def main():
	f = Person(50)
	print(f.getAge())
	print(f.getDecades())

	f.setAge(51)
	print(f.getAge())
	print(f.getDecades())

def main():
  
    p = Person(10)
    print("C++ Fibonacci:", p.fib())


    start = time.time()
    print("Python Fibonacci:", fib_py(10))
    print("Python Time:", time.time() - start)

 
    start = time.time()
    print("Numba Fibonacci:", fib_numba(10))
    print("Numba Time:", time.time() - start)
    
    
if __name__ == '__main__':
	main()
