## @file MoleculeT.py
#  @author Aditya Sharma
#  @brief This file contains the MoleculeT class.
from ChemEntity import *
from Equality import *
from ElmSet import *
from ChemTypes import *


## @brief This is a class that inherits from ChemEntity and Equality.
class MoleculeT(ChemEntity, Equality):
    ## @brief This is a constructor. It creates a MoleculeT object.
    #  @param n An natural number type.
    #  @param e An ElementT type.
    #  @return A MoleculeT type.
    #  @throw There are no exceptions.
    def __init__(self, n, e):
        self.__num = n
        self.__elm = e

    ## @brief It is a getter, it returns the number of atoms that an element has.
    #  @return A natural number. It represents the number of atoms in that molecule.
    def get_num(self):
        return self.__num

    ## @brief This is a getter method. Its purpose is to return the element in a molecule.
    #  @return A ElementT type. It represents the element in the molecule.
    def get_elm(self):
        return self.__elm

    ## @brief Its purpose is to find the number of atoms of a particular molecule.
    #  @param e This parameter is an ElementT type. It represents the element of a molecule.
    #  @return A natural number. It represents the occurences an atom shows up in an element
    def num_atoms(self, e):
        if e == self.get_elm():
            return self.get_num()
        else:
            return 0

    ## @brief Its purpose is to return a set of elements.
    #  @return An ElmSet type that represents a sequence of ElementT types.
    def constit_elems(self):
        return ElmSet([self.get_elm()])

    ## @brief Its purpose is to determine equality between two MoleculeT objects.
    #  @param m This parameter is a MoleculeT type. It represents a molecule.
    #  @return A boolean type. True signifies both molecules are the same; False doesn't.
    def equals(self, m):
        return (self.get_elm() == m.get_elm()) and (self.get_num() == m.get_num())
