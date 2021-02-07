#  reading a csv file and convert to dictionary of rows ( rows are dictionaries as well)
#  the values are converted to the correct type
#
#

import csv

# function to convert columns
clean = {
    'X': int, 'Y':int, 'month':str, 'day':str, 'FFMC':float,
    'DMC':float , 'DC':float, 'ISI':float ,'temp':float ,
    'RH':float , 'wind':float, 'rain':float , 'area':float
}

names = ['X','Y','month','day','FFMC','DMC','DC','ISI','temp','RH','wind','rain','area']



data = {}
with open('C:/Users/dev/code/forestfires.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)    
    for i, line in enumerate(reader):        
        row_dict = dict(zip(header, line))
        data[i] = { var: clean[var](val)
                    for  var, val in row_dict.items() }
        
#  using an iterator/generator, useful if the file is too big.


def feed_row( csv_iterator, row_cleaner):
    header = next(reader)
    while True:
        line = next(reader, None) 
        # adding None above will not raise StopIteration error
        if not line:
            break
        row_dict = dict(zip(header, line))
        row = { var: row_cleaner[var](val)
                    for  var, val in row_dict.items() if var in row_cleaner.keys()}
        yield row 
        
    
    
with open('C:/Users/dev/code/forestfires.csv', 'r') as f:
    reader = csv.reader(f)
    for r in feed_row(reader, clean):
        print(r)
    
    
# =============== Using DictRead 


import csv

csv_file = 'C:/Users/dev/code/forestfires.csv'

# function to convert columns
clean = {
    'X': int, 'Y':int, 'month':str, 'day':str, 'FFMC':float,
    'DMC':float , 'DC':float, 'ISI':float ,'temp':float ,
    'RH':float , 'wind':float, 'rain':float , 'area':float
}


# select the useful columns, can use clean above aswell.
clean_used_columns = {
    'month':str, 'day':str, 'temp':float ,
    'RH':float , 'wind':float, 'rain':float , 'area':float
}


with open(csv_file, 'r') as f:
    dreader = csv.DictReader(f)
    for r in dreader:    
        r_clean = { var: clean_used_columns[var](val)
                    for  var, val in r.items() if var in clean_used_columns.keys()}
        print(r_clean)



