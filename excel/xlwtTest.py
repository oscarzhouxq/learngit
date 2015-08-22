import xlwt
try:
	file = xlwt.Workbook()
	table = file.add_sheet("t1",cell_overwrite_ok=True)
	#for i in range()
	for i in range(10):
		for j in range(20):
			strt = "#"+str(i)+str(j)+"#dafdfads"
			table.write(i,j,strt)
			

	file.save("test.xls")
except Exception as e:
		print e