#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 03:12:52 2020

@author: VictorioMolina

Solving systems of equations with 3 unknowns
"""

import numpy as np

class SimultaneousEquations:
    def __init__(self, **kwargs):
        assert ('matrix' in kwargs and 'vector' in kwargs) \
               or 'file' in kwargs,\
            'You must specify either matrix/vector or file as parameters'
        
        assert len(kwargs) <= 2,\
            'The matrix/vector and file parameters are exclusive'
        
        self.solution = None
            
        if 'file' in kwargs:
            self.file = kwargs['file']
        else:
            self.file = None
            for k, v in kwargs.items():
                self.__setattr__(k, v)
    
    def __setattr__(self, name, value):
        v = value
        if name in ('matrix', 'vector'):
            v = v.copy()
            
        self.__dict__.update({name: v})
    
    def solve(self):
        if(not self.file):
            self.solution = np.linalg.solve(self.matrix, self.vector)
        else:
            # Leemos la matriz y el vector del fichero
            try:
                matrix_as_list = []
                vector_as_list = []
                with open(self.file) as f:
                    for line in f:
                        print("line", line)
                        if len(matrix_as_list) < 3:
                            matrix_as_list.append([float(n) for n in line.split()])
                        else:
                            vector_as_list.append(float(line))
                
                matrix = np.array(matrix_as_list)
                vector = np.array(vector_as_list)

                self.solution = np.linalg.solve(matrix, vector)
            except:
                print("Error in file format.")
                raise
                
    def save_to_file(self, file):
         save = input('Do you really want to exit ([y]/n)? ')
         if save == 'y':
             with open(file, 'w') as f:
                 if self.solution.all():
                     f.write(str(self.solution))
                 else:
                     f.write('No se ha resuelto el sistema.')
             
                 