import requests

import os 
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)

r.status_code

print(r.request.headers)

print("request body:", r.request.body)

header=r.headers
print(r.headers)

header['date']

header['Content-Type']

r.encoding

r.text[0:100]

# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

#make a get request
r=requests.get(url)

#response header
print(r.headers)

print(r.headers)

#image is response object, so save to file object 
path=os.path.join(os.getcwd(),'image.png')
path

with open(path,'wb') as f:
    f.write(r.content)

Image.open(path)  

#another example with Txt file
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'

r=requests.get(url)
path=os.path.join(os.getcwd(),'example1.txt')

with open(path,'wb') as f:
    f.write(r.content)

#get request with URL parameters
url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r=requests.get(url_get,params=payload)

r.url

print("request body:", r.request.body)

print(r.text)

r.headers['Content-Type']

#since content type is in json, we can format data as dict 
r.json()

#the key args has name and values 
r.json()['args']

#post requests
url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)

print("POST request URL:",r_post.url )
print("GET request URL:",r.url)

print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)

r_post.json()['form']




#new lab - Simple APIs - random user and Fruitvice API examples
'''
One of the applications we will use in this notebook is Random User Generator. RandomUser is an open-source, free API providing developers with randomly generated users to be used as placeholders for testing purposes. This makes the tool similar to Lorem Ipsum, but is a placeholder for people instead of text. The API can return multiple results, as well as specify generated user details such as gender, email, image, username, address, title, first and last name, and more. More information on RandomUser can be found here.

Another example of simple API we will use in this notebook is Fruitvice application. The Fruitvice API webservice which provides data for all kinds of fruit! You can use Fruityvice to find out interesting information about fruit and educate yourself. The webservice is completely free to use and contribute to.'''


!pip install randomuser

from randomuser import RandomUser
import pandas as pd

r = RandomUser()
some_list = r.generate_users(10)
some_list

name = r.get_full_name()

#only need 10 users with full names and emails.
for user in some_list:
    print (user.get_full_name()," ",user.get_email())
	
#get photos
for user in some_list:
    print (user.get_full_name()," ",user.get_email(), " ",user.get_picture())
	
#generate table with info about users 
def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     

get_users()

#create pandas dataframe
df1 = pd.DataFrame(get_users())  

#fruitvice API
import requests
import json

data = requests.get("https://www.fruityvice.com/api/fruit/all")
results = json.loads(data.text)

pd.DataFrame(results)

df2 = pd.json_normalize(results)
df2

#extract genus and family info from df for Cherry
cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

#how many calories in banana
banana = df2.loc[df2["name"] == 'Banana']
(banana.iloc[0]['nutritions.calories'])

results = json.loads(r.text)  #loads json content from json file into a dictionary
df = pd.DataFrame(results)


#example select multiple columns from dataframe
df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
df

# To select the 0th,1st and 2nd row of "First Name" column only
df.loc[[0,1,2], "First Name" ]

#show first five lines of dataframe
df.head(5)

#save data to csv
datatframe.to_csv("employee.csv", index=False)


#Data Formate	Read			Save
csv				pd.read_csv()	df.to_csv()
json			pd.read_json()	df.to_json()
excel			pd.read_excel()	df.to_excel()
hdf				pd.read_hdf()	df.to_hdf()
sql				pd.read_sql()	df.to_sql()


#count missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")  





#Extract API Data Lab
!mamba install pandas==1.3.3 -y
!mamba install requests==2.26.0 -y

import requests
import pandas as pd
import json

# Call the endpoint 
url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=Xyfr6aGVPJHvzPYWPD48nGBhJ8MpIWzf" #Make sure to change ******* to your API key.

# Turn the data into a dataframe
data=requests.get(url)

results = json.loads(data.text)
df=pd.DataFrame(results)
df

# Drop unnescessary columns
df_trim = df.drop(columns=['success', 'timestamp', 'base', 'date'])
df_trim

# Save the Dataframe to csv 
df_trim.to_csv('exchange_rates_1.csv')




