# Python3

import pandas as pd
import xml.etree.ElementTree as ET


tree = ET.parse('apple_health_export/export.xml')

root = tree.getroot()
record_list = [x.attrib for x in root.iter('Record')]


data = pd.DataFrame(record_list)


test = data[["type", "sourceName","unit", "creationDate", "startDate", "endDate", "value"]]


# type	sourceName	sourceVersion	unit	creationDate	startDate	endDate	value	device

final = test.to_csv("sample_health_data.csv", index=False)

print('done')

