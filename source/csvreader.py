import csv
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

def detect_type(values):
    """Guess column type from sample values"""

    for v in values:
        if v == "" or v is None:
            continue

        # try datetime
        try:
            datetime.strptime(v, "%H:%M:%S.%f")
            return "time"
        except ValueError:
            pass

        try:
            datetime.strptime(v, "%Y-%m-%d")
            return "date"
        except ValueError:
            pass

        # try numeric
        try:
            float(v)
            return "numeric"
        except ValueError:
            pass

    return "text"

#was times
val1 = []

#was sats
val2 = []

# Read CSV

csvfile=input("Enter filename: ")
with open(csvfile, newline='') as f:
    reader = csv.DictReader(f)
    data = list(reader)

    for x in reader.fieldnames:
        print(x)
    
    xval = input("Enter x value: ")
    yval = input("Enter y value: ")
    
    for y in data:

        if detect_type([y[xval]]) == "time":
            val1.append(datetime.strptime(y[xval], "%H:%M:%S.%f"))
        else:
            val1.append(float(y[xval]))
        
        if detect_type([y[yval]]) == "time":
            val2.append(datetime.strptime(y[yval], "%H:%M:%S.%f"))
        else:
            val2.append(float(y[yval]))

x = np.array(val1)
y = np.array(val2)

# sort by time
order = np.argsort(x)
x = x[order]
y = y[order]

step = 10  # show every 10th point

plt.figure(figsize=(1280/100, 1024/100), dpi=300)
plt.plot(x, y, marker='o')

plt.xlabel(xval)
plt.ylabel(yval)
plt.title("Plot of selected CSV columns")

plt.grid()
plt.savefig('output.png')
print("Saved graph to output.png")