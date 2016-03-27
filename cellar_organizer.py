#import filelib

# Load the csv file (eventually from the web)
inputFile = open("cellar_data.csv")

# Check that it actually opened the file
if inputFile.readable():
	print("The file is readable")
else:
	print("The file is not readable")

# Print out the first line
line = inputFile.readline().rstrip()
print(line)

# Grab the column headings
fields = line.split(",")
for field in fields:
	print(field)

print("Done with my test")
