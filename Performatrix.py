import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np


df = pd.concat(pd.read_excel('data.xlsx', sheet_name=None),ignore_index=True)
counts = (df['sem3']>4.75).value_counts()
#df['Did Pass'] = np.where(df['Sem5'].isnull(), np.nan, np.where(df['Sem5'] > 4.75, True, False))
#plt.pie(df['Did Pass'].value_counts([True,False]), labels=['Pass','Fail'], autopct='%1.1f%%', colors=['green', 'red'])
#plt.show()

#df['Did Pass'] = df['Sem5'].apply(lambda x: True if not np.isnan(x) and x > 4.75 else False if not np.isnan(x) else np.nan)
#print(df)
#df.to_csv('temp.txt', sep='\t', index=False)
#plt.pie(df['Did Pass'].value_counts(), labels=['Pass','Fail'], autopct='%1.1f%%', colors=['green', 'red'])



def graphs():
    df['mark_range3'] = pd.cut(df['sem3'], bins=[0, 4.75, 5.75, 6.75, 7.75, 10], labels=['Fail','>=4.75', '>=5.75', '>=6.75', '>=7.75'])
    df['mark_range4'] = pd.cut(df['sem4'], bins=[0, 4.75, 5.75, 6.75, 7.75, 10], labels=['Fail','>=4.75', '>=5.75', '>=6.75', '>=7.75'])
    df['mark_range5'] = pd.cut(df['Sem5'], bins=[0, 4.75, 5.75, 6.75, 7.75, 10], labels=['Fail','>=4.75', '>=5.75', '>=6.75', '>=7.75'])
    df['mark_range6'] = pd.cut(df['Sem6'], bins=[0, 4.75, 5.75, 6.75, 7.75, 10], labels=['Fail','>=4.75', '>=5.75', '>=6.75', '>=7.75'])
    df['mark_range7'] = pd.cut(df['SEM7'], bins=[0, 4.75, 5.75, 6.75, 7.75, 10], labels=['Fail','>=4.75', '>=5.75', '>=6.75', '>=7.75'])
    df['mark_range8'] = pd.cut(df['SEM8'], bins=[0, 4.75, 5.75, 6.75, 7.75, 10], labels=['Fail','>=4.75', '>=5.75', '>=6.75', '>=7.75'])
    df['Did Pass3'] = df['Did Pass'] = df['sem3'].apply(lambda x: True if not np.isnan(x) and x > 4.75 else False if not np.isnan(x) else np.nan)
    df['Did Pass4'] = df['Did Pass'] = df['sem4'].apply(lambda x: True if not np.isnan(x) and x > 4.75 else False if not np.isnan(x) else np.nan)
    df['Did Pass5'] = df['Did Pass'] = df['Sem5'].apply(lambda x: True if not np.isnan(x) and x > 4.75 else False if not np.isnan(x) else np.nan)
    df['Did Pass6'] = df['Did Pass'] = df['Sem6'].apply(lambda x: True if not np.isnan(x) and x > 4.75 else False if not np.isnan(x) else np.nan)
    df['Did Pass7'] = df['Did Pass'] = df['SEM7'].apply(lambda x: True if not np.isnan(x) and x > 4.75 else False if not np.isnan(x) else np.nan)
    df['Did Pass8'] = df['Did Pass'] = df['SEM8'].apply(lambda x: True if not np.isnan(x) and x > 4.75 else False if not np.isnan(x) else np.nan)

    # Style
    sns.set_style('darkgrid')


    # Set the figure size to the screen size
    plt.figure(figsize=(16,8))

    # SEM3 (bar)
    plt.subplot(2,6,1)
    plt.title('SEM 3', fontsize=14, fontweight='bold')
    sns.countplot(x="mark_range3", data=df,  color='blue')
    plt.ylabel('Count', fontsize=12)
    plt.xlabel('Marks Range', fontsize=12)
    plt.xticks(rotation=45)

    # SEM3 (pie)
    plt.subplot(2,6,7)
    plt.title('Pass/Fail Sem 3', fontsize=14, fontweight='bold')
    plt.pie(df['Did Pass3'].value_counts(), labels=['Pass','Fail'], autopct='%1.1f%%', colors=['green', 'red'])



    # SEM4 (bar)
    plt.subplot(2,6,2)
    plt.title('SEM 4', fontsize=14, fontweight='bold')
    sns.countplot(x="mark_range4", data=df,  color='green')
    plt.ylabel('Count', fontsize=12)
    plt.xlabel('Marks Range', fontsize=12)
    plt.xticks(rotation=45)

    # SEM4 (pie)
    plt.subplot(2,6,8)
    plt.title('Pass/Fail Sem 4', fontsize=14, fontweight='bold')
    plt.pie(df['Did Pass4'].value_counts(), labels=['Pass','Fail'], autopct='%1.1f%%', colors=['green', 'red'])



    # SEM5 (bar)
    plt.subplot(2,6,3)
    plt.title('SEM 5', fontsize=14, fontweight='bold')
    sns.countplot(x="mark_range5", data=df,  color='red')
    plt.ylabel('Count', fontsize=12)
    plt.xlabel('Marks Range', fontsize=12)
    plt.xticks(rotation=45)

    # SEM5 (pie)
    plt.subplot(2,6,9)
    plt.title('Pass/Fail Sem 5', fontsize=14, fontweight='bold')
    plt.pie(df['Did Pass5'].value_counts(), labels=['Pass','Fail'], autopct='%1.1f%%', colors=['green', 'red'])



    # SEM6 (bar)
    plt.subplot(2,6,4)
    plt.title('SEM 6', fontsize=14, fontweight='bold')
    sns.countplot(x="mark_range6", data=df,  color='purple')
    plt.ylabel('Count', fontsize=12)
    plt.xlabel('Marks Range', fontsize=12)
    plt.xticks(rotation=45)

    # SEM6 (pie)
    plt.subplot(2,6,10)
    plt.title('Pass/Fail Sem 6', fontsize=14, fontweight='bold')
    plt.pie(df['Did Pass6'].value_counts(), labels=['Pass','Fail'], autopct='%1.1f%%', colors=['green', 'red'])



    # SEM7 (bar)
    plt.subplot(2,6,5)
    plt.title('SEM 7', fontsize=14, fontweight='bold')
    sns.countplot(x="mark_range7", data=df,  color='orange')
    plt.ylabel('Count', fontsize=12)
    plt.xlabel('Marks Range', fontsize=12)
    plt.xticks(rotation=45)

    # SEM7 (pie)
    plt.subplot(2,6,11)
    plt.title('Pass/Fail Sem 7', fontsize=14, fontweight='bold')
    plt.pie(df['Did Pass7'].value_counts(), labels=['Pass','Fail'], autopct='%1.1f%%', colors=['green', 'red'])



    # SEM8 (bar)
    plt.subplot(2,6,6)
    plt.title('SEM 8', fontsize=14, fontweight='bold')
    sns.countplot(x="mark_range8", data=df,  color='brown')
    plt.ylabel('Count', fontsize=12)
    plt.xlabel('Marks Range', fontsize=12)
    plt.xticks(rotation=45)

    # SEM8 (pie)
    plt.subplot(2,6,12)
    plt.title('Pass/Fail Sem 8', fontsize=14, fontweight='bold')
    plt.pie(df['Did Pass8'].value_counts(), labels=['Pass','Fail'], autopct='%1.1f%%', colors=['green', 'red'])



    # Pass Fail (pie)
    #plt.subplot(2,5,9)
    #plt.title('Pass/Fail', fontsize=14, fontweight='bold')
    #plt.pie(df['Did Pass'].value_counts(), labels=['Pass', 'Fail'], autopct='%1.1f%%', colors=['green', 'red'])
    
    plt.suptitle("Student Performance Dashboard", fontsize=20, y=0.95, fontweight='bold')

    # Subplot spacing
    plt.tight_layout(pad=3)
    # Show figure
    plt.show()

graphs()