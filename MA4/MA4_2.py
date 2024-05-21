#!/usr/bin/env python3

from person import Person
from fibonacci import fib_py, fib_numba
import time
import matplotlib.pyplot as plt

def main():
	f = Person(50)
	print(f.getAge())
	print(f.getDecades())

	f.setAge(51)
	print(f.getAge())
	print(f.getDecades())

	p = Person(10)
	print("C++ Fibonacci:", p.fib())

	start = time.time()
	print("Python Fibonacci:", fib_py(10))
	print("Python Time:", time.time() - start)

	start = time.time()
	print("Numba Fibonacci:", fib_numba(10))
	print("Numba Time:", time.time() - start)

	x = range(20,30)
	y_py = []
	y_numba = []
	y_cpp = []

	for i in range(20, 30):
		start = time.time()
		Person(i)
		p.fib()
		y_cpp.append(time.time() - start)

	for i in range(20,30):
		start = time.time()
		fib_py(i)
		y_py.append(time.time() - start)

	for i in range (20,30):
		start=time.time()
		fib_numba(i)
		y_numba.append(time.time() - start)

	plt.plot(x, y_py)
	plt.plot(x, y_numba)
	plt.savefig("MA4.png")
	plt.show()
	print (y_py, y_numba)


if __name__ == '__main__':
	main()
