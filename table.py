from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.drawing.image import Image
from openpyxl import load_workbook

wb = load_workbook('Pie.xlsx')
ws = wb.active

tab = Table(displayName='Table1', ref='A1:B5')
#show first and last columns and have row and column stripes
style = TableStyleInfo(name='TableStyleMedium9',showFirstColumn=False, showLastColumn=False,
                                                    showRowStripes=True, showColumnStripes=True)
tab.tableStyleInfo = style
ws.add_table(tab)
wb.save('table.xlsx')

img = Image('madecraft.jpg')
img.width = img.width * .25
img.height = img.height * .25
ws.add_image(img, 'C1')
wb.save('new_image.xlsx')