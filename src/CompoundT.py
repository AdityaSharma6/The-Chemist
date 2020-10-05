## @file CompoundT.py
#  @author Aditya Sharma
#  @brief This file contains the CompoundT class

from MoleculeT import *
from ChemEntity import *
from Equality import *
from ElmSet import *
from MolecSet import *
from Set import *


## @brief This is a class for compounds
class CompoundT(ChemEntity, Equality):
    ## @brief This is a constructor.
    #  @param M It is a MolecSet type. It represents a sequence of MoleculeT types.
    def __init__(self, M):
        self.__C = M

    ## @brief This is a getter. Its purpose is to retrieve the MolecSet.
    #  @return A MolecSet type. It represents a sequence of MoleculeT types.
    def get_molec_set(self):
        return self.__C

    ## @brief This method finds the number of certain atoms in a molecular sequence.
    #  @param e This parameter is an ElementT type.
    #  @return An integer type. It represents the count of certain atoms in a sequence.
    def num_atoms(self, e):
        count = 0
        molecule_set = self.get_molec_set()
        sequence = molecule_set.to_seq()
        for i in range(len(sequence)):
            count += sequence[i].num_atoms(e)
        return count

    ## @brief This is a method that finds elements
    #  @return A ElmSet type. It represents elements from a molecule sequence.
    def constit_elems(self):
        array = []
        molecule_set = self.get_molec_set()
        sequence = molecule_set.to_seq()
        for i in range(len(sequence)):
            array.append(sequence[i].get_elm())
        return ElmSet(array)

    ## @brief This method determines if two sets of molecules are equal
    #  @param D This parameter is a moleculeT type.
    #  @return A boolean response. True means both molecule sets are equal. False does not.
    def equals(self, D):
        if self.get_molec_set().size() != D.get_molec_set().size(): 
            return False
        hashtable = {}
        for molecule in self.get_molec_set().to_seq():
            element = molecule.get_elm()
            element_count = molecule.get_num()
            if hashtable.get(element) is None:
                hashtable[element] = element_count
        for molecule in D.get_molec_set().to_seq():
            element = molecule.get_elm()
            element_count = molecule.get_num()
            if hashtable.get(element) is None:
                return False
            elif hashtable.get(element) != element_count:
                return False

        return True
