import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import plotly.express as px
import seaborn as sns
from scipy.spatial.distance import cityblock

#read_file
df = pd.read_csv('salary.csv')
print(df)


#list of columns names
print('\n *____________________ list of columns names ____________________*\n')
list_of_column_names = list(df.columns)
for x in range(0,len(list_of_column_names)):
	print(' ',x,' : ',list_of_column_names[x])


#type of columns
print('\n *______________________ type of columns   ______________________*\n')
print(df.dtypes)


#numbers of numerical columns
names=np.array(list_of_column_names)
columns=df.dtypes.tolist()
int_columns=0
int_columns_names=[]
float_columns=0
float_columns_names=[]
for x in range(0,len(list_of_column_names)):
	if columns[x]=='int64': 
		int_columns+=1
		int_columns_names.append(names[x])
	if columns[x]=='float64': 
		float_columns+=1
		float_columns_names.append(names[x])

#boolean columns
print('\n *______________________ boolean columns   ______________________*\n')
recogonize_boolean=np.array(int_columns_names)
boolean_columns=0
mean_columns=[]
for c in range(0,len(recogonize_boolean)):
	temp=0
	check_boolean=0
	check_boolean=df[recogonize_boolean[c]]
	z=0
	p=0
	for s in range(0,len(check_boolean)):	
		if check_boolean[s]==1 or check_boolean[s]==0:
			z+=1
		else:
			p+=1
	if z==len(check_boolean):
		boolean_columns+=1
		print(" ",recogonize_boolean[c])
	elif p==len(check_boolean):
		mean_columns.append(recogonize_boolean[c])

#number_fo_each_column_type
print(" ",len(list_of_column_names),"all columns")
print('  ----------------------')
print(" ",boolean_columns,"are boolean columns")
print(" ",float_columns,"are float columns")
print(" ",int_columns-boolean_columns,"are int columns")
object_columns=len(list_of_column_names)-(int_columns+float_columns)
print(" ",object_columns,"are object columns")


#mean of numerical columns
print('\n *_________________ mean of numerical columns   _________________*\n')
#print(mean_columns)
for m in range(0,len(mean_columns)):
	print(' \n ',mean_columns[m],' mean is:',df[mean_columns[m]].mean())
	
for n in range(0,len(float_columns_names)):
	print(' \n ',float_columns_names[n],'mean is:',df[float_columns_names[n]].mean())


#max of numerical columns
print('\n *_________________ max of numerical columns   _________________*\n')
for m in range(0,len(mean_columns)):
	print(' \n ',mean_columns[m],' max is:',df[mean_columns[m]].max())
	
for n in range(0,len(float_columns_names)):
	print(' \n ',float_columns_names[n],'max is:',df[float_columns_names[n]].max())


#min of numerical columns
print('\n *_________________ min of numerical columns   _________________*\n')
for m in range(0,len(mean_columns)):
	print(' \n ',mean_columns[m],' min is:',df[mean_columns[m]].min())
	
for n in range(0,len(float_columns_names)):
	print(' \n ',float_columns_names[n],'min is:',df[float_columns_names[n]].min())


#std of numerical columns
print('\n *___________  standard deviation of numerical columns ___________*\n')
for m in range(0,len(mean_columns)):
	print(' \n ',mean_columns[m],' std is:',df[mean_columns[m]].std())
	
for n in range(0,len(float_columns_names)):
	print(' \n ',float_columns_names[n],'std is:',df[float_columns_names[n]].std())


#uniqe count of numerical columns
print('\n *_________________ uniqe count of columns   _________________*\n')
for m in range(0,len(names)):
	print(' \n ',names[m],' count is:',df[names[m]].nunique())



#median of numerical columns
print('\n *______________  median of numerical columns _______________*\n')
for m in range(0,len(mean_columns)):
	print(' \n ',mean_columns[m],' median is:',df[mean_columns[m]].median())
	
for n in range(0,len(float_columns_names)):
	print(' \n ',float_columns_names[n],'median is:',df[float_columns_names[n]].median())



#variance of numerical columns
print('\n *_______________  variance of numerical columns _______________*\n')
for m in range(0,len(mean_columns)):
	print(' \n ',mean_columns[m],' variance is:',df[mean_columns[m]].var())
	
for n in range(0,len(float_columns_names)):
	print(' \n ',float_columns_names[n],'variance is:',df[float_columns_names[n]].var())



"""
#boxPlots
print('\n *___________  box plot for each numerical columns ___________*\n')
for m in range(0,len(mean_columns)):
	fig = plt.figure()
	manager = plt.get_current_fig_manager()
	manager.full_screen_toggle()
	fig.suptitle(mean_columns[m], fontsize=16)
	plt.boxplot(df[mean_columns[m]])
	plt.pause(3)
	plt.close()

for n in range(0,len(float_columns_names)):
	fig = plt.figure()
	manager = plt.get_current_fig_manager()
	manager.full_screen_toggle()
	plt.boxplot(df[float_columns_names[n]])
	fig.suptitle(float_columns_names[n], fontsize=16)
	plt.pause(3)
	plt.close()


mean_columns.remove('Age')

#HistogramPlots
print('\n *________  Histogram Plot for each numerical columns ________*\n')
for m in range(0,len(mean_columns)):
	commutes = pd.Series(df[mean_columns[m]],df['Age'])
	commutes.plot.hist(grid=True,bins=20, rwidth=0.9)
	plt.title('HistogramPlots')
	plt.xlabel(mean_columns[m])
	plt.ylabel('Age')
	plt.grid(axis='y', alpha=0.75)
	plt.pause(4)
	plt.close()

for n in range(0,len(float_columns_names)):
	commutes = pd.Series(df[float_columns_names[n]],df['Age'])
	commutes.plot.hist(grid=True, bins=20, rwidth=0.9)
	plt.title('HistogramPlots')
	plt.xlabel(float_columns_names[n])
	plt.ylabel('Age')
	plt.grid(axis='y', alpha=0.75)
	plt.pause(4)
	plt.close()


#ScatterPlots
print('\n *__________  Scatter Plot for each numerical columns __________*\n')
for m in range(0,len(mean_columns)):
	fig = plt.figure()
	manager = plt.get_current_fig_manager()
	manager.full_screen_toggle()
	plt.title('Scatter Plot')
	plt.xlabel(mean_columns[m])
	plt.ylabel('Age')
	plt.scatter(df['Age'],df[mean_columns[m]],color='red')
	plt.pause(4)
	plt.close()

for n in range(0,len(float_columns_names)):
	fig = plt.figure()
	manager = plt.get_current_fig_manager()
	manager.full_screen_toggle()
	plt.title('Scatter Plot')
	plt.xlabel(float_columns_names[n])
	plt.ylabel('Age')
	plt.scatter(df['Age'],df[float_columns_names[n]],color='red')
	plt.pause(4)
	plt.close()



mean_columns.apend(df['Age'])
#DistPlots
print('\n *__________  Dist Plot for each numerical columns __________*\n')
for m in range(0,len(mean_columns)):
	sns.histplot(df[mean_columns[m]],kde=True, stat="density", linewidth=0, 
             bins=int(180/5), color = 'orange')
	plt.title('DesityPlots')
	plt.xlabel(mean_columns[m])
	plt.ylabel('Dist')
	plt.grid(axis='y', alpha=0.75)
	plt.pause(4)
	plt.close()

for n in range(0,len(float_columns_names)):
	sns.histplot(df[float_columns_names[n]], kde=True, stat="density", linewidth=0, 
             bins=int(180/5), color = 'darkblue')
	plt.title('DesityPlots')
	plt.xlabel(float_columns_names[n])
	plt.ylabel('Dist')
	plt.grid(axis='y', alpha=0.75)
	plt.pause(4)
	plt.close()




#LinearPlots
print('\n *__________  Linear Plot for each numerical columns __________*\n')
for m in range(0,len(mean_columns)):
	fig = plt.figure()
	manager = plt.get_current_fig_manager()
	manager.full_screen_toggle()
	plt.title('Linear Plot')
	plt.xlabel(mean_columns[m])
	plt.ylabel('index')
	plt.plot(df['index'],df[mean_columns[m]],color='darkviolet')
	plt.pause(4)
	plt.close()

for n in range(0,len(float_columns_names)):
	fig = plt.figure()
	manager = plt.get_current_fig_manager()
	manager.full_screen_toggle()
	plt.title('Linear Plot')
	plt.xlabel(float_columns_names[n])
	plt.ylabel('index')
	plt.plot(df['index'],df[float_columns_names[n]],color='darkviolet')
	plt.pause(4)
	plt.close()

#PiePolt
labels=[]
sizes=[]
for m in range(0,len(names)):
	labels.append(names[m])
	sizes.append(len(names[m]))
fig = plt.figure()
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.pause(4)
plt.close()"""


#checkDistance
print("\n *________________________________________________________\n")
for m in range(0,len(mean_columns)):
	distance=[mean_columns[m]]
	da=pd.read_csv('salary.csv',usecols=distance)
	data=da.to_numpy()
	mid=len(data)/2
	mid=int(mid)

	F=[]
	for i in range(0,mid):
		F.append(data[i])

	S=[]
	for j in range(mid,len(data)):
		S.append(data[j])

	first_part_of_data=np.array(F)
	second_part_of_data=np.array(S)

	result=cityblock(first_part_of_data,second_part_of_data)
	print('\n Manhattan distance for',mean_columns[m],'is: ',result)

for n in range(0,len(float_columns_names)):
	distance=[float_columns_names[n]]
	da=pd.read_csv('salary.csv',usecols=distance)
	data=da.to_numpy()
	mid=len(data)/2
	mid=int(mid)

	F=[]
	for i in range(0,mid):
		F.append(data[i])

	S=[]
	for j in range(mid,len(data)):
		S.append(data[j])

	first_part_of_data=np.array(F)
	second_part_of_data=np.array(S)

	result=cityblock(first_part_of_data,second_part_of_data)
	print('\n Manhattan distance for',float_columns_names[n],'is: ',result)