""" Python interface to the C++ Person class """
import ctypes
import os

# Determine the absolute path to the shared library
current_dir = os.path.dirname(__file__)
lib_path = os.path.join(current_dir, 'libperson.so')
lib = ctypes.cdll.LoadLibrary(lib_path)

class Person:
    def __init__(self, age):
        self.obj = lib.Person_new(age)

    def getAge(self):
        return lib.Person_getAge(self.obj)

    def setAge(self, age):
        lib.Person_setAge(self.obj, age)

    def getDecades(self):
        return lib.Person_getDecades(self.obj)

    def fib(self):
        if hasattr(lib, 'Person_fib'):
            return lib.Person_fib(self.obj)
        else:
            raise NotImplementedError("The function Person_fib is not available in the shared library")

    def __del__(self):
        if hasattr(self, 'obj'):
            lib.Person_delete(self.obj)

# Specify the argument and return types for the C functions
lib.Person_new.argtypes = [ctypes.c_int]
lib.Person_new.restype = ctypes.c_void_p
lib.Person_getAge.argtypes = [ctypes.c_void_p]
lib.Person_getAge.restype = ctypes.c_int
lib.Person_setAge.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Person_setAge.restype = None
lib.Person_getDecades.argtypes = [ctypes.c_void_p]
lib.Person_getDecades.restype = ctypes.c_int

# Only set the argument and return types for Person_fib if it exists
if hasattr(lib, 'Person_fib'):
    lib.Person_fib.argtypes = [ctypes.c_void_p]
    lib.Person_fib.restype = ctypes.c_int

lib.Person_delete.argtypes = [ctypes.c_void_p]
lib.Person_delete.restype = None