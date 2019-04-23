import xlwt

book = xlwt.Workbook()


#Making a new sheet
sheet = book.add_sheet('Sheet1')

#adding a cell based on coordinates
sheet.write(0,0,'test_on_first_cell')
book.save('sample.xls')



IMDB-Movie-Data-xls
