# Importing the numpy library
import numpy as np

# Creating a 2D numpy array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculating the transpose of the matrix
# Columns become rows and rows become columns
transpose_matrix = np.transpose(matrix)

# Printing the original and transposed matrices
print("Original Matrix:")
print(matrix)
print("\nTransposed Matrix:")
print(transpose_matrix) 


# Learning slicing and indexing in numpy arrays
# Print first row

# Rule: [row_begin:row_end, column_begin:column_end]
first_row = matrix[0, :]

# Print second column
second_column = matrix[:, 1]
print("\nFirst Row:")
print(first_row)
print("\nSecond Column:") 
print(second_column)

# Using steps in slicing
# Print every second element from the first row
every_second_element = matrix[0, ::2]
print("\nEvery Second Element from First Row:")
print(every_second_element)

# Print elements from second row, starting from index 0 to 3 with a step of 2
step_elements = matrix[1, 0:3:2]
print("\nElements from Second Row with Step of 2:")
print(step_elements)

# Negative indexing to access elements from the end
# Print the last row
last_row = matrix[-1, :]
print("\nLast Row:")
print(last_row)

# Using negative is very powerful in numpy arrays for accessing elements from the end
# When size of array is not known, negative indexing helps in accessing elements easily
# When size is huge, negative indexing avoids the need to calculate the exact positive index
big_matrix = np.array([[i for i in range(100)] for j in range(100)])
last_five_elements = big_matrix[-1, -5:]
print("\nLast Five Elements of the Last Row in Big Matrix:")
print(last_five_elements)

# Saving and loading numpy arrays
# Saving the matrix to a file (binary format)  
np.save('matrix.npy', matrix)

# Loading the matrix from the file
# Explaining all params of np.load
# np.load(file, mmap_mode=None, allow_pickle=False, fix_imports=True, encoding
# file: The file to read. Can be a string or a file-like object.
# mmap_mode: If not None, then memory-map the file, using the given mode ('r+', 'r', 'w+', 'c').
# allow_pickle: Allow loading pickled object arrays stored in npy files. Default is False for security reasons.
# fix_imports: Only useful when loading Python 2 generated pickled files on Python
# encoding: The encoding used to decode pickled object arrays. Default is 'ASCII'.
loaded_matrix = np.load('matrix.npy', mmap_mode="r")
print("\nLoaded Matrix from File:")
print(loaded_matrix)

# Saving the matrix to a text file
# Explaining all params of np.savetxt
# np.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)
# fname: Filename or file handle to which the data is saved.
# X: Array-like data to be saved.
# fmt: Format string for the data.
# delimiter: String or character separating columns.
# newline: String or character separating lines.
# header: String that will be written at the beginning of the file.
# footer: String that will be written at the end of the file.
# comments: String that will be prepended to the header and footer strings.
# encoding: Encoding used to encode the output file. Default is None, which means system default
np.savetxt('matrix_float.txt', matrix, fmt='%.5f')

# Loading the matrix from the text file
loaded_text_matrix = np.loadtxt('matrix.txt')   
print("\nLoaded Matrix from Text File:")
print(loaded_text_matrix)


