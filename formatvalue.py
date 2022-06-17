import openpyxl
from openpyxl_image_loader import SheetImageLoader
wb = openpyxl.load_workbook("result.xlsx")
# print(wb.sheetnames)
sheet1 = wb['DANHSACHDOANVIEN']



# sheet1["D13"] = "aaaa"
# wb.save("craw.xlsx")

# xu li ten
def rename(col,a,b):
	list_name = []
	process_list_name = []
	for i in range(a,b):
		cell = sheet1[col+str(i)]
		list_name.append(cell.value)
	for i in list_name:
		k = i.split(" ")
		temp = []
		for j in k:
			if j != "":
				x = j[0].upper()+j[1:len(j)]
				temp.append(x)
		temp = " ".join(temp)
		process_list_name.append(temp)
		# print(temp)
	return process_list_name

#xu li thang nam
def change_dob(col,a,b):
	list_date = []
	process_list_date = []
	for i in range(a,b):
		cell = sheet1[col+str(i)]
		list_date.append(cell.value)
	for i in list_date:
		if str(type(i)) == "<class 'NoneType'>":
			process_list_date.append("")
		else:
			i=str(i)
			if len(i) == 4:
				ngay = i[0]
				thang = i[1]
				nam = i[2:]
				if int(nam) < 21:
					result = ngay+"/"+thang+"/20"+nam
				else:
					result = ngay+"/"+thang+"/19"+nam
				process_list_date.append(result)
			elif len(i) == 6:
				ngay = i[0:2]
				thang = i[2:4]
				nam = i[4:]
				if int(nam) < 21:
					result = ngay+"/"+thang+"/20"+nam
				else:
					result = ngay+"/"+thang+"/19"+nam
				process_list_date.append(result)
			elif len(i)==5:
				ngay = i[0:1]
				thang = i[1:3]
				nam = i[3:]
				if int(nam) < 21:
					result = ngay+"/"+thang+"/20"+nam
				else:
					result = ngay+"/"+thang+"/19"+nam
				process_list_date.append(result)
	return process_list_date
def change_date_CD(col,a,b):
	list_date = []
	process_list_date = []
	for i in range(a,b):
		cell = sheet1[col+str(i)]
		list_date.append(cell.value)
	for i in list_date:
		if str(type(i)) == "<class 'NoneType'>":
			process_list_date.append("28/07/2019")
		else:
			if len(i) == 4:
				ngay = i[0]
				thang = i[1]
				nam = i[2:]
				result = ngay+"/"+thang+"/20"+nam
				process_list_date.append(result)
			elif len(i) == 6:
				ngay = i[0:2]
				thang = i[2:4]
				nam = i[4:]
				result = ngay+"/"+thang+"/20"+nam
				process_list_date.append(result)
			else:
				process_list_date.append("bug ne")
	return process_list_date


# cell = sheet1["C7"]
# print(type(cell.value))
# print(str(type(cell.value)) == "<class 'NoneType'>")
#check cmnd
def check_id_card(col,a,b):
	temp = a
	list_id = []
	for i in range(a,b):
		cell = sheet1[col+str(i)]
		list_id.append(cell.value)
	for i in range(len(list_id)):
		if len(list_id[i]) != 9 and len(list_id[i]) !=12:
			print(col+str(temp))
		temp+=1
# check_id_card("G",7,166)


# for i in change_dob('D',61,166):
# 	print(i)

# listName = rename('E',7,166)
# for i in listName:
# 	print(i)

