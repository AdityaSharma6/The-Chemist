## @file ChemEntity.py
#  @author Aditya Sharma
#  @brief The file contains an interface.

from abc import ABC, abstractmethod


##  @brief An interface that will be used later on to implement particular behaviours.
class ChemEntity(ABC):
    ## @brief This is an abstract method. It returns the number of atoms in an element.
    #  @param elm This parameter an an ElementT Type.
    @abstractmethod
    def num_atoms(self, elm):
        pass

    ## @brief This is an abstract method.
    @abstractmethod
    def constit_elems(self):
        pass
