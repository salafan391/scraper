import plotly.express as px
import pandas as pd
try:
    df = pd.read_csv('data_files/rafed_data.csv')
    df['تاريخ الوفاة ميلادي']= df['تاريخ الوفاة ميلادي'].apply(pd.to_datetime)
except:
    print('no file')
def sex_pie(date):
    start_date = date
    specific_date=df[df['تاريخ الوفاة ميلادي']>=start_date]
    sex = specific_date['النوع'].value_counts()
    fg = px.pie(sex,values=sex.values,title= f'{sex.values} نسبة الوفيات من الذكور والإناث',names=sex.index)
    fg.show()
def cleaners_pie(date):
    start_date = date
    specific_date=df[df['تاريخ الوفاة ميلادي']>=start_date]
    cleaners = specific_date['المغسل'].value_counts()
    fg = px.pie(cleaners,values=cleaners.values,title=f'{cleaners.values} نسبة غسل الوفيات بحسب المغسل',names=cleaners.index)
    fg.show()
def centers_pie(date):
    start_date = date
    specific_date = df[df['تاريخ الوفاة ميلادي'] >= start_date]
    center = specific_date['إسم المغسلة'].value_counts()
    
    fg=px.pie(center,values=center.values,title=f' {center.values} نسبة غسل الوفيات في المراكز',names=center.index)
    fg.show()

