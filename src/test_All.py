## @file test_All.py
#  @author Aditya Sharma
#  @brief This file is the test file.

from Set import *
from MoleculeT import *
from CompoundT import *
from ReactionT import *
import pytest


class TestSet:

	def setup_method(self, method):
		self.setA = Set([1, 2, 3, 4, 5])
		self.setB = Set([5, 4, 3, 2, 0])
		self.setC = Set([3, 2, 1, 4, 5])

	def teardown_method(self, method):
		self.setA = None

	def test_add_a(self):
		self.setA.add(5)
		assert self.setA.size() == 5

	def test_add_b(self):
		self.setA.add(6)
		assert self.setA.size() == 6
		assert self.setA.member(6) == True

	def test_rm(self):
		with pytest.raises(ValueError):
			self.setA.rm(6)

	def test_member_a(self):
		assert self.setA.member(5) == True

	def test_member_b(self):
		assert self.setA.member(6) == False

	def test_size(self):
		assert self.setA.size() == 5

	def test_equals_a(self):
		assert self.setA.equals(self.setB) == False

	def test_equals_b(self):
		assert self.setA.equals(self.setC) == True

	def test_to_seq(self):
		assert self.setA.to_seq() == [1,2,3,4,5]


class TestMoleculeT:
	def setup_method(self, method):
		self.moleculeA = MoleculeT(2, ElementT.H)
		self.moleculeB = MoleculeT(1, ElementT.H)
		self.moleculeC = MoleculeT(2, ElementT.H)
		self.moleculeD = MoleculeT(2, ElementT.O)
	
	def teardown_method(self, method):
		self.moleculeA = None
		self.moleculeB = None
		self.moleculeC = None
		self.moleculeD = None

	def test_get_num(self):
		assert self.moleculeA.get_num() == 2

	def test_get_elm(self):
		assert self.moleculeA.get_elm() == ElementT.H

	def test_num_atoms_a(self):
		assert self.moleculeA.num_atoms(ElementT.H) == 2

	def test_num_atoms_b(self):
		assert self.moleculeA.num_atoms(ElementT.S) == 0

	def test_constit_elems_a(self):
		assert type(self.moleculeA.constit_elems()) == type(ElmSet([ElementT.H]))

	def test_constit_elems_b(self):
		assert self.moleculeA.constit_elems().to_seq() == [ElementT.H]

	def test_equals_a(self):
		assert self.moleculeA.equals(self.moleculeB) == False
	
	def test_equals_b(self):
		assert self.moleculeA.equals(self.moleculeC) == True
	
	def test_equals_c(self):
		assert self.moleculeA.equals(self.moleculeD) == False


class TestCompoundT:
	def setup_method(self, method):
		self.moleculeA = MoleculeT(2, ElementT.H)
		self.moleculeB = MoleculeT(1, ElementT.S)
		self.moleculeC = MoleculeT(4, ElementT.O)
		self.moleculeD = MoleculeT(2, ElementT.O)

		self.molecSetA = MolecSet([self.moleculeA, self.moleculeB, self.moleculeC])
		self.molecSetB = MolecSet([self.moleculeA, self.moleculeD])

		self.compoundA = CompoundT(self.molecSetA)
		self.compoundB = CompoundT(self.molecSetB)
	
	def teardown_method(self, method):
		self.moleculeA = None
		self.moleculeB = None
		self.moleculeC = None
		self.moleculeD = None

		self.molecSetA = None
		self.molecSetB = None

		self.compoundA = None
		self.compoundB = None
	
	def test_get_molec_set(self):
		assert self.compoundA.get_molec_set().to_seq() == MolecSet([self.moleculeA, self.moleculeB, self.moleculeC]).to_seq()
	
	def test_num_atoms_a(self):
		assert self.compoundA.num_atoms(ElementT.H) == 2

	def test_num_atoms_b(self):
		assert self.compoundA.num_atoms(ElementT.Be) == 0

	def test_constit_elems(self):
		assert set(self.compoundA.constit_elems().to_seq()) == set(ElmSet([ElementT.H, ElementT.S, ElementT.O]).to_seq())

	def test_equals_a(self):
		assert self.compoundA.equals(self.compoundA) == True
	
	def test_equals_b(self):
		assert self.compoundA.equals(self.compoundB) == False


class TestReactionT:
	def setup_method(self, method):
		
		self.moleculeA = MoleculeT(4, ElementT.C)
		self.moleculeB = MoleculeT(10, ElementT.H)

		self.moleculeC = MoleculeT(2, ElementT.O)

		self.moleculeD = MoleculeT(1, ElementT.C)
		self.moleculeE = MoleculeT(2, ElementT.O)

		self.moleculeF = MoleculeT(2, ElementT.H)
		self.moleculeG = MoleculeT(1, ElementT.O)

		self.molecSetA = MolecSet([self.moleculeA, self.moleculeB])
		self.molecSetB = MolecSet([self.moleculeC])
		self.molecSetC = MolecSet([self.moleculeD, self.moleculeE])
		self.molecSetD = MolecSet([self.moleculeF, self.moleculeG])

		self.compoundA = CompoundT(self.molecSetA)
		self.compoundB = CompoundT(self.molecSetB)
		self.compoundC = CompoundT(self.molecSetC)
		self.compoundD = CompoundT(self.molecSetD)

		self.reactionA = ReactionT([self.compoundA, self.compoundB], [self.compoundC, self.compoundD])
	
	def teardown_method(self, method):
		self.moleculeA = None
		self.moleculeB = None

		self.moleculeC = None

		self.moleculeD = None
		self.moleculeE = None

		self.moleculeF = None
		self.moleculeG = None

		self.molecSetA = None
		self.molecSetB = None
		self.molecSetC = None
		self.molecSetD = None

		self.compoundA = None
		self.compoundB = None
		self.compoundC = None
		self.compoundD = None
	
	def test_get_lhs(self):
		assert self.reactionA.get_lhs() == [self.compoundA, self.compoundB]

	def test_get_rhs(self):
		assert self.reactionA.get_rhs() == [self.compoundC, self.compoundD]

	def test_get_lhs_coeff(self):
		assert self.reactionA.get_lhs_coeff() == [1,6.5]

	def test_get_rhs_coeff(self):
		assert self.reactionA.get_rhs_coeff() == [4,5]
