import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/home/pankaj/mytime.csv")
print (df)
y = (df.iloc[:,1])
x = (df.iloc[:,0])
plt.plot(x,y, marker ='o')
plt.subplots_adjust(bottom=0.04, top=0.79)
locs, labels = plt.xticks()
plt.xlabel('Time')
plt.ylabel('Latency')
plt.title('Latency over time Without Proxy')
plt.setp(labels, rotation=-90)
plt.show()
