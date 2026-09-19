def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	# Let the matrices be a_ij and n_kl

    # Check if it doesn't align
    if len(a[0]) != len(b):
        return -1
    
    # Elif it aligns:
    c = []
    for i in range(len(a)):
        per_row = []  # i-th a_row multiplied by every b_col
        for k in range(len(b[0])):
            cross_product = 0  # i-th a_row multiplied by k-th b_col
            for j in range(len(a[0])):
                cross_product += a[i][j] * b[j][k]
            per_row.append(cross_product)
        c.append(per_row)
    
    return c