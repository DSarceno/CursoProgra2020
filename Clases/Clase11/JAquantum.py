'''
    JAquantum.py

    September 5, 2020
    José Alfredo de León

    This module conatains useful functions to use
    in quantum mechanics computations.
'''

import numpy as np
from itertools import product, combinations
import sys

# Pauli matrices:
s1 = np.array([[0,1],[1,0]])        # sigma_x
s2 = np.array([[0,-1j],[1j,0]])     # sigma_y
s3 = np.array([[1,0],[0,-1]])       # sigma_z

# Array with identity matrix and 3 Pauli matrices
sigma = np.array([np.identity(2),s1,s2,s3])

# Computational 2D basis (eigenbasis of s3)
ket0 = np.array([[0],[1]])
ket1 = np.array([[1],[0]])
zEigenbasis = np.array([ket0,ket1])

def Pauli(indices):
    '''
    Recursive function to calculate the tensor product of
    Pauli matrices.

    Examples:
    Pauli([1,2]) = sigma_x tensor sigma_y
    Pauli([2,3,0]) = sigma_y tensor sigma_z tensor identity
    '''
    if len(indices) == 0:
        return 1
    else:
        return np.kron(sigma[indices.pop(0)], Pauli(indices))


def TensorZkets(indices):
    '''
    Recursive function to calculate the tensor product of
    the elements from the eigenbasis of sigma_z.

    Examples:
    TensorZkets([1,0]) = ket1 tensor ket0
    TensorZkets([1,1,1,1]) = ket1 tensor ket1 tensor ket1 tensor ket1
    '''
    if len(indices) == 0:
        return 1
    else:
        return np.kron(zEigenbasis[indices.pop(0)], TensorZkets(indices))


def Comm(A, B):
    '''
    Calculates the commutator of two matrices A and B.

    Example:
    Comm(A,B) = AB - BA
    '''
    return np.matmul(A, B) - np.matmul(B, A)

def diagonalMatrix(dim, diagEntries):
    '''
    Constructs a diagonal square matrix.

	dim : dimension of the matrix, int expected
	diagEntries : list with diagonal entries, list expected
    '''
    if (type(dim) != int):
        sys.exit("Integer expected as first argument of diagonalMatrix function.")

    if (type(diagEntries) != list):
        sys.exit("List expected as second argument of diagonalMatrix function.")

    if (len(diagEntries) != dim):
        sys.exit("In diagonalMatrix function: length of diagonal-entries' list does not match dimension of the matrix.")

    A = np.zeros((dim, dim))

    for i in range(dim):
        A[i][i] = diagEntries[i]

    return A

def combinations_of_components(n, num_of_corr):
	rIndices = list(range(4**n-1))

	positions = list(combinations(rIndices, num_of_corr))

	r = np.zeros((len(positions),4**n))

	for i in range(len(positions)):
		r[i][0] = 1
		for j in positions[i]:
			r[i][j+1] = 1
	return r

def maps_in_Pauli_basis(n, param, num_of_corr):
    '''
    Constructs, in the Pauli basis, all the posible maps that leave invariant a certain qbit-system's number of components.

    Input:
    - n: number of qbits
    - param: number of maps to consider (usually depends on the number of components to leave invariant)
    - num_of_corr: number of components to leave invariant

    Returns an array with param number of all possible maps that leave invariant the num_of_corr n-qbit-system's number of components.
    '''
    # Storage all possible combinations of arrays of size 4**n with num_of_corr ones and the rest zeroes
    r = combinations_of_components(n, num_of_corr)

    # Create an array to storage the param number of maps (square matrices of size 4**n)
    maps_P = np.zeros((param, 4**n, 4**n))

    # Assign to every diagonal element of every map its correspondent element in each array of posible combinations of 1's and 0's
    for i in range(param):
        for j in range(4**n):
            maps_P[i][j][j] = r[i][j]

    # Return all possible maps in the Pauli basis
    return maps_P


def onesAndZeros(oneIndices, listLength):
	# Construct a list of 1's and 0's from tuple of indices of 1's.

	#if ( (type(oneIndices) != tuple) or (type(oneIndices) != list)):
	#	sys.exit("List or a tuple expected as argument of onesAndZeros.")

	List = [0]*(listLength)

	for i in oneIndices:
		List[i] = 1

	return List

def change_of_basis_matrix_P_to_C(n):
	alpha = [0,1,2,3]
	R = np.array(list(product(alpha, repeat=(n))))

	# Create a 2D square array to storage in each row every vector of the Pauli basis
	change_of_basis_M = np.zeros((4**n, 4**n))

	# Actually asign to each row of change_of_basis_M every vector of the Pauli basis
	for i in range(4**n):
		dummy = np.identity(2**n)
		for j in range(n):
			dummy = dummy @ S(n,R[i][j],j+1)
		change_of_basis_M[i] = dummy.reshape(4**n)

	# Now that you have each column in every row of the change-of-basis matrix in change_of_basis_M transpose it to get the actual
	# change-of-basis matrix
	# M_cb_PaC = np.column_stack(change_of_basis_M)
	change_of_basis_M = change_of_basis_M.T

	return change_of_basis_M

def reshuffle(A, n):
	'''
	Computes the reshuffling of a square matrix of size 4**n.

	Input:
	- A: 2D squared np.array
	- n: number of qbits in the system

	Returns the dynamical matrix (also known as Choi matrix) of A.
	'''
	# Calculate the dimension of the density matrix of the qbit system
	rho_size = 2**n

	# Create a 2D square array to storage the dynamical matrix
	dynamical_Matrix = np.zeros((4**n,4**n))

	# Compute the reshuffling of A
	k = 0 # qbit number label (?)
	p = 0 # index of the rows after every row in A has been reshaped in a square matrix of size 2**n
	for i in range(4**n): # Go over each of the 4**n rows of D
		if i % rho_size == 0 and i != 0: # If it has completed a rho_size number of rows of A
			k = k + 1
			p = 0
		for j in range(rho_size): # Each iteration goes over 4**n elements in a row of D
			dynamical_Matrix[i][rho_size*j:rho_size*(j+1)] = A[rho_size*k+j].reshape((rho_size,rho_size))[p]
		p = p + 1

	return dynamical_Matrix

def chop(expr, *, max=1e-10):
	return [i if abs(i) > max else 0 for i in expr]

def positivity_test(A):
    '''
    Checks the positivity of a matrix.

    Input:
    - A: matrix

    Returns a boolean value. True if A is indeed positive and false if it's not.
    '''
    # Calculate the smallest eigenvalue of A
    smallest_eig = chop(np.linalg.eigh(A)[0])[0]

    # Compute the logical value of the positivity
    positivity = smallest_eig >= 0
    return positivity

# The following function was provided by A. Cabrera. Many thanks to him.
def matrix_form(matrix, limiter='p'):
    """
    Pretty print of a matrix with different delimiters depending on 'p', 'b'or 'v'
    """
    if limiter == 'p':
        ls, li = '⎛', '⎝'
        rs, ri = ' ⎞', ' ⎠'
    elif limiter == 'b':
        ls, li = '⎡', '⎣'
        rs, ri = ' ⎤', ' ⎦'
    elif limiter == 'v':
        ls, li = '⎢', '⎢'
        rs, ri = ' ⎥', ' ⎥'
    else:
        ls, li = '⎡', '⎣'
        rs, ri = ' ⎤', ' ⎦'
    max = 0
    for row in matrix:
        for ele in row:
            if len(str(ele)) > max:
                max = len(str(ele))
    print_str = ''
    for i in range(len(matrix)):
        if i == 0:
            print_str += f'{ls}'
        elif i==(len(matrix)-1):
            print_str += f'{li}'
        else:
            print_str += '⎢'
        for j in range(len(matrix[i])):
            print_str += ' {val:^{max}}'.format(val=matrix[i][j], max=max)
        if i == 0:
            print_str += f'{rs}\n'
        elif i==(len(matrix)-1):
            print_str += f'{ri}'
        else:
            print_str += ' ⎥\n'
    print(print_str, end='\n\n')
    return
