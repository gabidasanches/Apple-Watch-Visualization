# Apple-Watch-Visualization

Python (pandas, ElementTree) and Tableau
  - Apple Watch Visualization project - exported the data in XML format from my apple watch and used Python, pandas and ElementTree to clean the data, extract information and create a useful excel table.
  - Used the excel table in Tableau to create visuals to understand the data exported from my apple watch

TechStacK
  - Python
  - Tableuea 

For Python, I used the following libraries, Pandas and ElementTree. Apple produces exported data in the form of an XML via the Apple Watch. I used the Python library ElementTree, to access the root of the XML file, in order to then parse the file into readable structures for Ptyhon. 

Once the XML file was readable, I then stored the output in a Pandas dataframe, where I was able to to get a readbale snapshot of the data, which helped me filter and extract my data. I then took this and extracted data, and used Pandas (.to_csv()) to create a CSV file of the output data I needed for Tableau

In Tableau I extracted the data from the table and I filtered the information to create different visuals. 

Once the table was exported I created a bar graph to visualize the step counts in 2021 on each month.
