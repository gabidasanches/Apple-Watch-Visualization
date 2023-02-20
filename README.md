# Apple-Watch-Visualization

After using my Apple Watch for 3 years, I was interested in seeing how my activity has changed since covid-19 began. Now enrolled in my MS analytics program, I have the tools to now investigate how my health has changed since covid started.

Data Process: 
Apple allows health data to be exported from the device, however, this data is packaged into an XML file, not readable to people. I used Python, specifically the ElementTree library in order to parse this XML data. Once readable to some degree, I then took this converted data and ran it through a Pandas dataframe to get more insight into how the data was described and to make it easier to view with the goal of storing the final output in the form of an csv file. With the data in csv format, it was easier to read and understand, which allowed me to decide what columns I needed to use to extrapolate data from my Apple Watch. I then took the needed data, and cloned it to an xlsx file to isolate any changes, which I then uploaded to a Tableau view to visualize my health data!


Tech Stack:
  - Python
  - Tableuea
  - Excel
  - XML
  
# Tech Stack Summary: Python/XML (pandas, ElementTree) and Excel/Tableau

For Python, I used the following libraries, Pandas and ElementTree. Apple produces exported data in the form of an XML via the Apple Watch. I used the Python library ElementTree, to access the root of the XML file, in order to then parse the file into readable structures for Python. 

![Screenshot 2023-02-20 at 5 27 50 PM](https://user-images.githubusercontent.com/123784158/220207305-798966e9-b474-4769-8eac-20b55391e7b3.png)



Once the XML file was readable, I then stored the output in a Pandas dataframe, where I was able to to get a readbale snapshot of the data, which helped me filter and extract my data. I then took this and extracted data, and used Pandas (.to_csv()) to create a CSV file of the output data I needed for Tableau

In Tableau I extracted the data from the table and I filtered the information to create different visuals. 

Once the table was exported I created a bar graph to visualize the step counts in 2021 on each month.
