import pandas as pd

data_x = {'Student':["David","Samuel","Terry","Evan"],
          'Age':["27","24","22","32"], 
          'Country':["UK","Canada","China","USA"], 
          'Course':["Python","Data Structures","ML","Software Dev"], 
          'Marks':["33","56","88","23"], 
         }
df = pd.DataFrame(data_x)

b = df[["Marks"]]
c = df[["Country","Course"]]
d = df["Country"]

#loc[row_label, column_label]
# iloc[row_index, column_index]

vals = df.iloc[0, 0] # Access the value on the first row and the first column
vals_col = df.loc[0, 'Student'] # Access the column using the name
#Creating new Dataframe & Student column as an index colum
newDF=df
newDF=newDF.set_index("Student")
newDF.head() #To display the first 5 rows of new dataframe

#access the column using the name
accessedCol = newDF.loc['David', 'Age']

#Slicing uses the [] operator to select a set of rows and/or columns from a DataFrame.
#To slice out a set of rows, you use this syntax: data[start:stop],

sliced = df.iloc[0:3, 0:3]

#slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
sliced_2 = df.loc[0:2,'Student':'Age']

#slicing using loc() function on new dataframe df2 where index column is Name having labels: Rose, John and Jane
sliced_3 = newDF.loc['David':'Samuel', 'Age':'Marks']


