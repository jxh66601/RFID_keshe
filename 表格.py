import openpyxl
list=[['卡号','打卡时间']]
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='门禁考勤表'
for item in list:
    sheet.append(item)
wb.save('考勤表.xlsx')