import openpyxl
from openpyxl_image_loader import SheetImageLoader
wb = openpyxl.load_workbook("D:\\office\\craw.xlsx")
print(wb.sheetnames)
sheet1 = wb['DANHSACHDOANVIEN']
img_load = SheetImageLoader(sheet1)
local = "imgexcel//"
for_mat = ".png"
print(sheet1)
for i in range(8,32):
	celle8 = sheet1['E'+str(i)]
	file_name = celle8.value

	i = img_load.get('F'+str(i))

	i.save(local+str(file_name)+for_mat)