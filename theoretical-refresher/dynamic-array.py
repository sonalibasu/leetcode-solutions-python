"""
Custom implementation of a dynamic array ie. python list.
Doing this in python using the ctypes library.
"""

import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0                                  #actual count
        self.capacity = 1   
        self.A = self.make_array(self.capacity)
    
    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        if not 0<= k <self.n:    #if not valid index
            return IndexError('Index is out of bounds')
        return self.A[k]

    def append(self,elem):
        if self.n == self.capacity:
            self._resize(2*self.capacity)    

        self.A[self.n] = elem
        self.n += 1       

    def _resize(self,new_cap):      
        B = self.make_array(new_cap) # New bigger array
        
        for k in range(self.n): # Reference all existing values
            B[k] = self.A[k]
            
        self.A = B # Call A the new bigger array
        self.capacity = new_cap # Reset the capacity
        
    def make_array(self,new_cap):
        return (new_cap * ctypes.py_object)()