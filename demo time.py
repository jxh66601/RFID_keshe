import openpyxl
list=[['卡的卡号','刷卡时间']]
if __name__ == '__main__':

    wb = openpyxl.Workbook()
    sheet = wb.active

    # 更改默认名称Sheet`
    sheet.title = "门禁考勤表"

    for item in list:
        sheet.append(item)

    # 保存
    wb.save('考勤表.xlsx')
    print('ok')