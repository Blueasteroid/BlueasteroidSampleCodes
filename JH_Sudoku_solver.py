### JH Sudoku solver 2024-11-03
import matplotlib.pyplot as plt
import numpy as np
sudoku=np.asarray([[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]])
def sudoku_print(sudoku = sudoku):
	print('----------------------------')
	for x in range(9):
		for y in range(9):
			if y==0:
				print('| ', end='')
			if sudoku[x,y] ==0:
				print('_ ',end='')
			else:
				print(str(sudoku[x,y]) +' ', end='')
			if (y+1)%3==0:
				print(' | ',end='')
			if (y+1)%9==0:
				print(' ')
		if (x+1)%3==0 :
			print('----------------------------')
def sudoku_element_3D_check(sudoku = sudoku, x=0, y=0):
	row = sudoku[x,:]
	col = sudoku[:,y]
	cellx= ((x)//3)*3 +np.array([0,1,2])
	celly= ((y)//3)*3 +np.array([0,1,2])
	xx, yy = np.meshgrid(cellx, celly)
	cell = sudoku[xx,yy].flatten()
	arr3d= np.concatenate((row,col,cell), axis=None)
	unique_arr= np.unique(arr3d)
	test=np.array([0,1,2,3,4,5,6,7,8,9])
	mask=np.isin(test, unique_arr)
	rest=test[~mask]
	return rest
def JH_sodoku_solver(sudoku = sudoku):
	arr = sudoku.copy()
	step=0
	while(np.sum(arr)<405):
		for x in range(9):
			for y in range(9):
				if arr[x,y]==0:
					rest = sudoku_element_3D_check(arr, x=x, y=y)
					if len(rest)==1:
						step+=1
						arr[x,y]= rest[0]
						print(f'step={step},x={x},y={y},ans={rest[0]}')
	sudoku_print(sudoku)
	sudoku_print(arr)
if __name__ == '__main__':
	JH_sodoku_solver()
