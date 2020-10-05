## @file reactionT.py
#  @author Aditya
#  @brief This file contains the ReactionT
#  Online citation: https://stackoverflow.com/questions/45220032/how-to-balance-a-chemical-equation-in-python-2-7-using-matrices


from MoleculeT import *
from ChemTypes import *
from ChemEntity import *
from Equality import *
from ElmSet import *
from MolecSet import *
from Set import *
import numpy as np


## @brief This class is responsible for balancing a chemical equation
class ReactionT:
    ## @brief This is a constructor
    #  @param L This parameter is a sequence of CompoundT types.
    #  @param R This parameter is a sequence of CompoundT types.
    def __init__(self, L, R):
        self.__lhs = L
        self.__rhs = R

        try:
            left_coeffs, right_coeffs = self.__balancer()
            if is_balanced(L, R, left_coeffs, right_coeffs) and pos(left_coeffs) and pos(right_coeffs):
                self.__coeffL, self.__coeffR = left_coeffs, right_coeffs
        except:
            raise ValueError

    ## @brief This getter retrives the compound sequence on the left side of the equation
    #  @return A sequence of CompoundT types.
    def get_lhs(self):
        return self.__lhs

    ## @brief This getter retrives the compound sequence on the right side of the equation
    #  @return A sequence of CompoundT types.
    def get_rhs(self):
        return self.__rhs

    ## @brief This getter retrieves a real number sequence from the equation's left side.
    #  @return A real number sequence. It represents the coefficient values of each compound
    def get_lhs_coeff(self):
        return self.__coeffL

    ## @brief This getter retrieves a real number sequence from the equation's right side.
    #  @return A real number sequence. It represents the coefficient values of each compound
    def get_rhs_coeff(self):
        return self.__coeffR

    ## @brief This is a local function used to balance equations
    #  @return 2 sequences of real numbers representing the coefficients of both sides
    #  Citation: Jash, Zackary (Discussion & Debug)
    def __balancer(self):
        all_elements = elm_in_chem_eq(self.get_lhs()).to_seq()
        all_compounds = []

        # Create array of compounds
        for i in range(len(self.get_lhs())):
            all_compounds.append(self.get_lhs()[i])
        for i in range(len(self.get_rhs())):
            all_compounds.append(self.get_rhs()[i])

        # AX = B and we are solving for X
        b = []
        a = []

        for i in range(len(all_elements)):
            singular_element = all_elements[i]
            count_of_atoms = self.get_lhs()[0].num_atoms(singular_element)
            b.append(count_of_atoms)

        for i in range(len(all_elements)):
            temp = []
            for j in range(1, len(all_compounds)):
                singular_element = all_elements[i]
                element_counter = all_compounds[j].num_atoms(singular_element)
                temp.append(element_counter)
            a.append(temp)

        # Numpy Linear Equation Solver
        x = np.linalg.lstsq(a, b, rcond=-1)
        left_coeffs = [1]
        right_coeffs = []

        # Get coefficients for left and right sides by traversing X
        for i in range(len(self.get_lhs()) - 1):
            left_coeffs.append(round(x[0][i], 3))
        for i in range(len(self.get_lhs()) - 1, len(self.get_rhs()) + len(self.get_lhs()) - 1):
            right_coeffs.append(round(x[0][i], 3))
        
        # Eliminate negatives
        for i in range(len(left_coeffs)):
            if left_coeffs[i] < 0:
                left_coeffs[i] = abs(left_coeffs[i])

        return left_coeffs, right_coeffs


## @brief This static method ensures every element within a sequence is positive.
#  @param s This parameter is a sequence of real numbers.
#  @return A boolean type. True signifies that every element is positive. False doesn't.
def pos(s):
    for i in range(len(s)):
        if s[i] < 0:
            return False
    return True


## @brief This static method finds the count of an atoms in a sequence of compounds.
#  @param C This parameter is a sequence of CompoundT types.
#  @param c This parameter is a sequence of real numbers. It represents the coefficients
#  @param e This parameter is a ElementT type. It represents the element.
#  @return A natural number type. This represents the count of the atoms.
def n_atoms(C, c, e):
    count = 0
    for i in range(len(C)):
        count += c[i] * C[i].num_atoms(e)
    return count


## @brief This method finds the set of elements from each compound in a given sequence.
#  @param C This parameter is a sequence of CompoundT types.
#  @return This method returns an sequence of ElementT type.
def elm_in_chem_eq(C):
    element_seq = C[0].constit_elems()
    for compound in C:
        compound_element_seq = compound.constit_elems()
        for elements in compound_element_seq.to_seq():
            element_seq.add(elements)
    return element_seq


## @brief This local function checks if the count of atoms of an element is equal.
#  @param L This parameter is a sequence of CompoundT types.
#  @param R This parameter is a sequence of CompoundT types.
#  @param cL This parameter is a sequence of real number types.
#  @param cR This parameter is a sequence of real number types.
#  @return A Boolean type. True signifies that equivalent counts of atoms. False doesn't.
def is_bal_elm(L, R, cL, cR, e):
    return n_atoms(L, cL, e) == n_atoms(R, cR, e)


## @brief This local function checks if both sides are balanced
#  @param L This parameter is a sequence of CompoundT types.
#  @param R This parameter is a sequence of CompoundT types.
#  @param cL This parameter is a sequence of real number types.
#  @param cR This parameter is a sequence of real number types.
#  @return A boolean type. True signifies balance. False doesn't.
def is_balanced(L, R, cL, cR):
    left = elm_in_chem_eq(L)
    right = elm_in_chem_eq(R)
    for element in left.to_seq():
        if not is_bal_elm(L, R, cL, cR, element):
            return False
    return (left.equals(right))