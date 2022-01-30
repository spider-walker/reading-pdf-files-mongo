

# importing all the required modules
from tabula import read_pdf
from tabulate import tabulate

df = read_pdf("./data/2017.pdf",pages="all") #address of pdf file
print(tabulate(df))