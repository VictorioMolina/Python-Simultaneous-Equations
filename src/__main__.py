#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 03:07:07 2020

@author: VictorioMolina
"""

import numpy as np

from simultaneous_equations import SimultaneousEquations

def main():
    se = SimultaneousEquations(file="file.txt")
    se.solve()
    se.save_to_file("solution.txt")
    
if __name__ == '__main__':
    main()