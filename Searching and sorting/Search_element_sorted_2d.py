'''
Given a 2D grid(sorted both row wise and column wise), search for an element
'''

def search(mat, key):
	i, j = 0, len(mat[0])-1
	while i < len(mat) and j >= 0:
		if mat[i][j] == key:
			return True, i, j
		elif mat[i][j] > key:
			j -= 1
		else:
			i += 1
	return False

if __name__ == "__main__":
	matrix = [[10, 20, 30, 40],
			  [15, 25, 35, 45],
			  [24, 29, 37, 48],
			  [32, 33, 39, 50]]

	for k in [10, 20, 15, 30,48, 50, 47, 51, 100, 0]:
		print(k, search(matrix, k))
		