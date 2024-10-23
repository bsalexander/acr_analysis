import tabula

# # Read pdf into a list of DataFrame
# dfs = tabula.read_pdf("/workspaces/acr_analysis/Acute Nonlocalized Abdominal Pain", pages='all')

# for table in dfs:
#     print(table)

tabula.convert_into("Acute Nonlocalized Abdominal Pain.pdf", "output.csv", output_format="csv", pages='all')  