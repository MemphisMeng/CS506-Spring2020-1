def determinant(matrix):
	if matrix is None:
		return
	if len(matrix) <= 0 or len(matrix[0]) <= 0 or len(matrix) != len(matrix[0]):
		return

	if len(matrix) == 2:
		return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

	sum = 0
	for i in range(len(matrix)):
		firstRow = matrix[0]
		Matrix = matrix[1:]
		for j in range(len(firstRow)):
			Matrix[j] = Matrix[j][:i] + Matrix[j][i+1:]

		sign = (-1) ** (i / 2)
		sum += sign * determinant(Matrix) * firstRow[i]

	return sum