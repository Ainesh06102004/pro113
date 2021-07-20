import csv
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import statistics
import  numpy as np
import random

df=pd.read_csv('Saving_data.csv')
fig=px.scatter(df,y='quant_saved',color='rem_any')
fig.show()



with open('Saving_data.csv',newline="") as f:
  reader=csv.reader(f)
  savings_data=list(reader)
  savings_data.pop(0)
print(savings_data)

total_entries=len(savings_data)
total_people_given_reminder=0

for data in savings_data:
  if int(data[3])==1:
    total_people_given_reminder+=1

fig=go.Figure(go.Bar(x=['Reminded','Not reminded'],
              y=[total_people_given_reminder,
              (total_entries-total_people_given_reminder)]))
fig.show()



all_savings=[]
for data in savings_data:
  all_savings.append(float(data[0]))

mean_of_savings=statistics.mean(all_savings)
median_of_savings=statistics.median(all_savings)
mode_of_savings=statistics.mode(all_savings)

print("Mean of Savings=",mean_of_savings)
print("Median of Savings=",median_of_savings)
print("Mode of Savings=",mode_of_savings)


reminder_savings=[]
not_reminder_savings=[]

for data in savings_data:
  if int(data[3])==1:
    reminder_savings.append(float(data[0]))

  else:
    not_reminder_savings.append(float(data[0]))

mean_reminder=statistics.mean(reminder_savings)
median_reminder=statistics.median(reminder_savings)
mode_reminder=statistics.mode(reminder_savings)

mean_not_reminder=statistics.mean(not_reminder_savings)
median_not_reminder=statistics.median(not_reminder_savings)
mode_not_reminder=statistics.mode(not_reminder_savings)


print("Mean of reminder",mean_reminder)
print("Median of reminder",median_reminder)
print("Mode of reminder",mode_reminder)
print("\n\n")
print("Mean of not reminder",mean_not_reminder)
print("Median of not reminder",median_not_reminder)
print("Mode of reminder",mode_not_reminder)


print(f"Standard deviation of all the data->{statistics.stdev(all_savings)}")

print(f"Standard deviation of reminder data->{statistics.stdev(reminder_savings)}")
print(f"Standard deviation of not reminder data->{statistics.stdev(not_reminder_savings)}")


age=[]
savings=[]
for data in savings_data:
  if float(data[5])!=0:
     age.append(float(data[5]))
     savings.append(float(data[0]))
   


correlation=np.corrcoef(age,savings)
print("Correlation ",correlation [0,1])

fig=ff.create_distplot([df['quant_saved'].tolist()],['Savings'],show_hist=False)
fig.show()



import seaborn as sns
sns.boxplot(data=df,x=df['quant_saved'])
q1=df['quant_saved'].quantile(0.25)
q3=df['quant_saved'].quantile(0.75)
iqr=q3-q1
print(f"q1-{q1}")
print(f"q3-{q3}")
print(f"iqr-{iqr}")


lower_whisker=q1-1.5*iqr
upper_whisker=q3+1.5*iqr
print(f"lowerWhisker-{lower_whisker}")
print(f"upperWhisker-{upper_whisker}")


new_df=df[df['quant_saved']<upper_whisker]
all_savings=new_df['quant_saved'].tolist()

mean=statistics.mean(all_savings)
median=statistics.median(all_savings)
mode=statistics.mode(all_savings)
stdev=statistics.stdev(all_savings)
print("Mean of new data",mean)
print("Median of new data",median)
print("Mode of new data",mode)
print("Standard deviation=",stdev)


fig=ff.create_distplot([all_savings],['Savings'],show_hist=False)
fig.show()

sampling_mean_list=[]
for i in range(1000):
  temp_list=[]
  for j in range(100):
    temp_list.append(random.choice(all_savings))
  
  sampling_mean_list.append(statistics.mean(temp_list))

mean_sample=statistics.mean(sampling_mean_list)
print("Mean of sample=",mean_sample)



fig=ff.create_distplot([sampling_mean_list],['Mean of sampling '],show_hist=False)
fig.add_trace(go.Scatter(x=[mean_sample,mean_sample],y=[0,0.1],mode='lines',name='mean'))
fig.show()


print(f"Standard deviation of sampling mean list-{statistics.stdev(sampling_mean_list)}")
print(f"Mean of population-{statistics.mean(all_savings)}")
print(f"Mean sample-{mean_sample}")

reminded_df = new_df.loc[new_df["rem_any"] == 1] 
not_reminded_df = new_df.loc[new_df["rem_any"] == 0]
print(reminded_df.head())
print(not_reminded_df.head())

fig = ff.create_distplot([not_reminded_df["quant_saved"].tolist()], 
                         ["Savings (Not Reminded)"], show_hist=False) 
fig.show()