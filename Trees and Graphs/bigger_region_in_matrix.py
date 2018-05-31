matrix1= [[1, 0, 1, 0, 1],
          [1, 1, 0, 0, 0],
          [0, 1, 0, 1, 1]]


matrix2= [[0,0,0,1,1,0,0],
          [0,1,0,0,1,1,0],
          [1,1,0,1,0,0,1],
          [0,0,0,0,0,1,0],
          [1,1,0,0,0,0,0],
          [0,0,0,1,0,0,0]]


matrix3= [[0,0,0,1,0,0,0],
          [0,1,0,0,0,1,0],
          [1,1,0,1,0,0,1],
          [0,0,0,0,0,0,0],
          [1,1,0,0,0,0,0],
          [0,0,0,1,0,0,0]]


def get_region_size(matrix, row, column):
  if row < 0 or row >= len(matrix) or column < 0 or column >= len(matrix[0]):
    return 0

  if matrix[row][column] == 0:
    return 0

  matrix[row][column] = 0
  size = 1
  
  for x in range(row-1, row+2):
    for y in range(column-1, column+2):
      size += get_region_size(matrix, x, y)

  return size


def get_bigger_region(matrix):
  max_region = 0
  all_regions = []

  for row in range(len(matrix)):
    for column in range(len(matrix[0])):
      if matrix[row][column] == 1:
        size = get_region_size(matrix, row, column)
        max_region = max(max_region, size)
        all_regions.append('({}, {}) : {}'.format(row, column, size))

  print("All regions: ", ', '.join(all_regions))
  return max_region


print("Bigger region: ", get_bigger_region(matrix1))
print("Bigger region: ", get_bigger_region(matrix2))
print("Bigger region: ", get_bigger_region(matrix3))

