## @file Set.py
#  @author Aditya Sharma
#  @brief This file contains the Set class.

from Equality import *
## @brief Inherits from the "Equality" class.


class Set(Equality):
    ## @brief This is a constructor. It creates a Set object.
    #  @param s This parameter is a sequence containing elements of a particular type.
    def __init__(self, s):
        self.S = set(s)

    ## @brief This mutator adds elements of a particular type to the Set object.
    #  @param e It is of the same data type as the other elements in the set.
    def add(self, e):
        self.S.add(e)

    ## @brief This mutator removes elements of a particular type from the Set object.
    #  @param e It is of the same data type as the other elements in the set.
    #  @throw ValueEror It is thrown if an element is being removed that doesn't exist.
    def rm(self, e):
        try:
            self.S.remove(e)
        except:
            raise ValueError

    ## @brief This method checks if the given input is a member of the set.
    #  @param e It is of the same data type as the other elements in the set.
    #  @return A boolean type. True signifies the input is a member and False doesn't.
    def member(self, e):
        new_set = set([e])
        return new_set.issubset(self.S)

    ## @brief This is a getter.
    #  @return A natural number (integer) type. It represents the length of the set.
    def size(self):
        return len(self.S)

    ## @brief This method determies if the input set is equal to the given set.
    #  @param r It is a sequence of the same type as the elements in the Set object.
    #  @return A boolean type. True signifies that set equivalence and False doesn't.
    def equals(self, r):
        return set(r.to_seq()) == self.S

    ## @brief This method creates a sequencial representhation of the set.
    #  @return A list type. It represents a sequence of data types.
    def to_seq(self):
        return list(self.S)
