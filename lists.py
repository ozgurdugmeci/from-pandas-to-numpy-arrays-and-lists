import pandas as pd

pathy="C:\\Users\\Ozgur\\Desktop\\htm\\graph.xlsx"
df=pd.read_excel(pathy, 'data')
df.columns=['cinsiyet','isim']
#print(df.head(10))

table = pd.pivot_table(df, values=['cinsiyet'], index=['isim'], aggfunc='count')

#table.columns = table.columns.droplevel(0) #remove amount
table.columns.name = None               #remove categories
table = table.reset_index()                #index to columns

table=table.head(15)
df3=table.as_matrix()


liste= df3.tolist()
print(liste[0])




