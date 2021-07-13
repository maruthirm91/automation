import pandas as pd
import requests

df=pd.read_excel("C:/Users/Maruthi-PC/Desktop/urlfile.xlsx")

print('Converting list to dictionary...')
link=df['link']
id=df['ID']
df_dict=dict(zip(id,link))
print('list is converted to dictionary!!')

#iterating over the web links from the excel read earlier and stored in df.
for key, value in df_dict.items():
    print('sending HTTP requests for: ', key)
    r=requests.get(value)
    if value.find('.'):  #finding the '.' from the URL to locate the file extension
        extn='.'+ value.rsplit('.',1)[1] #retrieving the word after '.'. Usually the file download URL's will have file extensions as last string
        name='APU-'+str(key)+str(extn) # appending the Key value from dictionary to file extension and name it to file being downloaded
    with open(name,'wb') as f:
        f.write(r.content) # writing the content of response recieved from HTTP request.

print('files downloaded')
