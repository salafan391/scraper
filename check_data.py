import pandas as pd
df = pd.read_csv('rafed_data.csv')
def check_data():
    try:
        def full_func(value):
            if isinstance(value,float):
                return len(str(value).split('.')[0])
            elif isinstance(value,str) and value[0] != '0':
                return len(value)
            elif value[0] == '0':
                return len(value[1:]) 
        def check_id(value):
            value = str(value)
            if value != '10':
                return 'x'
            else:
                return ''

        def check_phone(value):
            value = str(value)
            if value != '9':
                return 'x'
            else:
                return ''

        df['id_rep'] = df['رقم هوية المبلغ '].apply(full_func)
        df['phone_rep'] = df['رقم تليفون المبلغ'].apply(full_func)

        df['id_w1'] = df['رقم هوية الشاهد الأول'].apply(full_func)
        df['phone_w1']=df['رقم تلفون الشاهد الأول'].apply(full_func)

        df['id_w2'] = df['رقم هوية الشاهد الثاني'].apply(full_func)
        df['phone_w2']=df['رقم تلفون الشاهد الثاني'].apply(full_func)

        clean_df = df[df['رقم تلفون الشاهد الأول'].notna()]
        w1 = clean_df[['الشاهد الأول','id_w1','phone_w1']].query("id_w1 !=10 | phone_w1 != 9")
        w2 = clean_df[['الشاهد الثاني','id_w2','phone_w2']].query("id_w2 !=10 or phone_w2 != 9")
        reporters = df[['اسم المبلغ','id_rep','phone_rep']].query('id_rep !=10 | phone_rep != 9')
        w1['phone_w1']=w1['phone_w1'].apply(check_phone)
        w1['id_w1']=w1['id_w1'].apply(check_id)
        reporters['id_rep'] = reporters['id_rep'].apply(check_id)
        reporters['phone_rep'] = reporters['phone_rep'].apply(check_phone)
        w2['id_w2'] = w2['id_w2'].apply(check_id)
        w2['phone_w2'] = w2['phone_w2'].apply(check_phone)
        w1.rename(columns={'id_w1' : 'رقم البطاقة','phone_w1':'رقم الجوال'},inplace=True)
        w2.rename(columns={'id_w2' : 'رقم البطاقة','phone_w2':'رقم الجوال'},inplace=True)
        reporters.rename(columns={'id_rep' : 'رقم البطاقة','phone_rep':'رقم الجوال'},inplace=True)
        dfs = [reporters,w1,w2]
        for i in range(0,len(dfs)):
            dfs[i].to_excel(f'x{i}.xlsx')
    except:
        print('لا يوجد أخطاء')




