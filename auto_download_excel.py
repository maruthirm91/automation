import pandas as pd
import requests

df=pd.read_excel("C:/Users/Maruthi-PC/Desktop/urlfile.xlsx")

print('Converting list to dictionary...')
link=df['link']
id=df['ID']
df_dict=dict(zip(id,link))
print('list is converted to dictionary!!')

for key, value in df_dict.items():
    print('sending HTTP requests for: ', key)
    r=requests.get(value)
    if value.find('.'):
        extn='.'+ value.rsplit('.',1)[1]
        name='APU-'+str(key)+str(extn)
    with open(name,'wb') as f:
        f.write(r.content)

print('files downloaded')