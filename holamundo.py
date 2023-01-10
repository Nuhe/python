import openpyxl
file = "cest.xlsx"

excel_document = openpyxl.load_workbook(file) #Cargamos el archivo en una variable

excel_document.get_sheet_names()  #Con get_sheet_names() obtenemos las hojas de nuestro archivo
sheet = excel_document.get_sheet_by_name("Hoja1") #Obtenemos la ubicacion de las celdas. No el contenido.
#print(sheet["A2"].value) Obtenemos el valor de una celda en especifica. Solo UN valor.

#Lo siguiente es para saber el TIPO de una celda.
#print type(sheet['A2'])                         
#print sheet.cell(row = 5, column = 2)           

#ACCEDIENDO A MULTIPLES CELDAS (RANGO)
multiple_cells = sheet['A1':'B3'] #Cargamos un rango de celdas
for row in multiple_cells: # Recorremos el rango de celdas pero no obtenemos ningun valor todavia.
    for cell in row: # Aca si obtenemos el valor de las celdas en el rango.
        if cell.value == "Hola Gato": #Mira tilin. Si usas el metodo value, se fija en el valor dentro de la celda.
            print(cell)

#ACCEDIENDO A TODAS LAS FILAS Y COLUMNAS
all_rows = sheet.rows
all_rows = list(all_rows) #Ojo aca Tiliiiin. all_rows te tira TypeError: 'generator' object is not subscriptable. Por eso lo convertimos en lista.
print(all_rows[:])

all_columns = sheet.columns
all_columns = list(all_columns)
print(all_columns[:])