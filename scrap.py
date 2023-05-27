import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
class Scrap:
    columns = [ "اسم المتوفي","النوع","الفئة العمرية","العمر","محل الإقامة","العنوان",'تاريخ الوفاة','رقم هوية المتوفي','سبب الوفاة','الشهود','حالة جسد المتوفى','اسم المبلغ','رقم هوية المبلغ ','رقم تليفون المبلغ','جهة المبلغ','علاقته بالمتوفى','تصريح الدفن','الغسل','صلاة الجنازة', 'الدفن', 'النعى','رقم التصريح', 'جهة التصريح', 'تاريخ التصريح','إسم المغسلة','المغسل', 'مكان الغسل','عنوان الغسل','إسم المسجد','مكان المسجد','يوم', 'عقب صلاة', 'إسم المقبرة','مكان المقبرة', 'عنوان المقبرة', 'رقم الصف','رقم المربع','رقم القبر', 'تاريخ الدفن', 'اسم السيارة','نوع السيارة', 'السائق','مسار السيارة']
    def __init__(self,url,username,password,count):
        self.url = url
        self.usernsme = username
        self.password = password
        self.count = count
        self.session = requests.session()
        login_page = self.session.get(self.url)
        login_soup = bs(login_page.content,'html.parser')
        csrf_token = login_soup.find('input',{'name':'token'})['value']
        self.combined_data = []
        self.login_data = {
            'token':csrf_token,
            'login_username':self.usernsme,
            'login_password': self.password}
        self.data_table = ''
        self.dict_data = {}
        for column_name in self.columns:
            self.dict_data[column_name] = [] 
        print(len(self.dict_data))
        self.get_login_page()
        self.get_data()
        self.combine_data()
    def get_login_page(self):
        response = self.session.post(self.url,data=self.login_data)
        if response.status_code == 200:
            print('login was successfull')
        else:
            print('login faild',response.status_code)
    def get_data(self):
        for i in range(self.count):
            data_url = f'https://www.muasah.org.sa/rafed/_view_final_reports.php?id={i}'
            data_page = self.session.get(data_url)
            soup = bs(data_page.content, 'html.parser')
            table = soup.find_all('table','data_table')
            self.data_table+=str(table)    
    def combine_data(self):
        group_size = 10
        self.data_table = self.data_table.replace('[]','')
        df = pd.read_html(self.data_table)
        groups = []
        # Iterate over the list in chunks of group_size
        for i in range(0, len(df), group_size):
            group = df[i:i+group_size]
            groups.append(group)
        self.combined_data = [pd.concat(groups[i]).set_index(0) for i in range(len(groups))]
        for i in self.combined_data:
            self.dict_data["اسم المتوفي"].append(i.loc['الإسم/الرقم التعريفى'][1])
            self.dict_data['النوع'].append(i.loc['الإسم/الرقم التعريفى'][3])
            self.dict_data['الفئة العمرية'].append(i.loc['الفئة العمرية'][1])
            self.dict_data['العمر'].append(i.loc['الفئة العمرية'][3])
            self.dict_data['محل الإقامة'].append(i.loc['محل الإقامة'][1])
            self.dict_data['العنوان'].append(i.loc['محل الإقامة'][3])
            self.dict_data['تاريخ الوفاة'].append(i.loc['تاريخ الوفاة'][1])
            self.dict_data['رقم هوية المتوفي'].append(i[1][4])
            self.dict_data['سبب الوفاة'].append(i.loc['سبب الوفاة'][1])
            self.dict_data['الشهود'].append(i.loc['شهود واقعة الوفاة'][1])
            # # self.dict_data['الشاهد الأول'].append(i[''])
            # # self.dict_data['رقم هوية الشاهد الأول'].append(i[''])
            # # self.dict_data['رقم تلفون الشاهد الأول'].append(i[''])
            # # self.dict_data['الشاهد الثاني'].append(i[''])
            # # self.dict_data['رقم هوية الشاهد الثاني'].append(i[''])
            # # # self.dict_data['رقم تلفون الشاهد الثاني'].append(i[''])
            self.dict_data['حالة جسد المتوفى'].append(i.loc['حالة جسد المتوفى'][1])
            self.dict_data['اسم المبلغ'].append(i.loc['الإسم'][1])
            self.dict_data['رقم هوية المبلغ '].append(i[1][9])
            self.dict_data['رقم تليفون المبلغ'].append(i.loc['الإسم'][3])
            self.dict_data['جهة المبلغ'].append(i.loc['رقم الهوية او الإقامة'][3][1])
            self.dict_data['علاقته بالمتوفى'].append(i.loc['علاقته بالمتوفى'][1])
            self.dict_data['تصريح الدفن'].append(i['الحالة'][11])
            self.dict_data['الغسل'].append(i['الحالة'][12])
            self.dict_data['صلاة الجنازة'].append(i['الحالة'][13])
            self.dict_data['الدفن'].append(i['الحالة'][14])
            self.dict_data['النعى'].append(i['الحالة'][15])
            self.dict_data['رقم التصريح'].append(i.loc['رقم التصريح'][1])
            self.dict_data['جهة التصريح'].append(i.loc['رقم التصريح'][3])
            self.dict_data['تاريخ التصريح'].append(i.loc['تاريخ التصريح'][1])
            self.dict_data['إسم المغسلة'].append(i.loc['إسم المغسلة'][1])
            self.dict_data['المغسل'].append(i.loc['المغسل'][1])
            self.dict_data['مكان الغسل'].append(i.loc['مكان الغسل'][1])
            self.dict_data['عنوان الغسل'].append(i.loc['مكان الغسل'][3])
            self.dict_data[ 'إسم المسجد'].append(i.loc['إسم المسجد'][1])
            self.dict_data['مكان المسجد'].append(i.loc['المكان'])
            self.dict_data['يوم'].append(i.loc['يوم'][1])
            self.dict_data['عقب صلاة'].append(i.loc['يوم'][3])
            self.dict_data['إسم المقبرة'].append(i.loc['إسم المقبرة'][1])
            self.dict_data['مكان المقبرة'].append(i.loc['المكان'][1])
            self.dict_data['عنوان المقبرة'].append(i.loc['المكان'][3])
            self.dict_data['رقم الصف'].append(i.loc['رقم الصف'][1])
            self.dict_data['رقم المربع'].append(i.loc['رقم الصف'][3])
            self.dict_data['رقم القبر'].append(i.loc['رقم القبر'][1])
            self.dict_data['تاريخ الدفن'].append(i.loc['تاريخ الدفن'][1])
            self.dict_data['اسم السيارة'].append(i.loc['اسم السيارة'][1])
            self.dict_data['نوع السيارة'].append(i.loc['اسم السيارة'][3])
            self.dict_data['السائق'].append(i.loc['السائق'][1])
            self.dict_data['مسار السيارة'].append(i.loc['مسار السيارة'][1])
        df = pd.DataFrame(self.dict_data)
        df.to_csv('rafed_data.csv')
