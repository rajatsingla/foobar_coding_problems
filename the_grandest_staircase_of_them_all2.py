def P(maxn):
	matrix=[[0 for i in range(maxn)] for i in range(maxn)]
	for n in range(3,maxn+1):
		for m in range(n-1,1,-1):
			tmp=0
			if m>(n-m):
				tmp=1
			tmp+=sum(matrix[n-m-1][:m-1])
			matrix[n-1][m-1]=tmp
	return matrix





print P(4)
