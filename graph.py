import openpyxl
from openpyxl.chart import PieChart, Reference, Series, PieChart3D

wb = openpyxl.Workbook()
ws = wb.active

data = [
    ['Flavor', 'Sold'],
    ['Vanilla', 1500],
    ['Chocolate', 1700],
    ['Strawberry', 600],
    ['Pumpkin Spice', 950]
]

for rows in data: 
    ws.append(rows) #automatically appends at A1 starting

chart = PieChart() #inform Excel how to map and use chart
labels = Reference(ws,min_col=1,min_row=2,max_row=5) #don't need to specify max_col because it is the same as our min of 1)
data = Reference(ws, min_col=2, min_row=1, max_row=5)
chart.add_data(data,titles_from_data=True)
chart.set_categories(labels)
chart.title = 'Ice Cream by Flavor'

ws.add_chart(chart, 'C1') #setting to C1 because data ends at B column
wb.save('Pie.xlsx')