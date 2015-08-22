#coding=utf-8
import xlrd
try:
	data = xlrd.open_workbook("test.xls")
	table = data.sheets()[0]
	#print dir(table.cell[0][1])
	print "行数有,",table.nrows,"列数有",table.ncols
	print table.cell(0,0).value
	print "打印....."
	for row in range(table.nrows):
		for col in range(table.ncols):
			print table.cell(row,col).value
except Exception as e:
	print e