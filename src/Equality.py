## @file Equality.py
#  @author Aditya
#  @brief This file contains the Equality class.
from abc import ABC, abstractmethod


## @brief An interface that will be used later on to implement particular behaviours.
class Equality(ABC):
    ## @brief This is an abstract method.
    #  @param t This parameter is a sequence.
    @abstractmethod
    def equals(self, t):
        pass
