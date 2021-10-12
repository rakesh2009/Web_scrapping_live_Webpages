from bs4 import BeautifulSoup
import requests
import pandas as pd

html=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
# print(html) #if we print this we get output as 'response-200' that means request done successfully. but we want 'html text' for this we use 'html.text'#
html_text=html.text
# print(html_text) #here we get entire html text#

soup=BeautifulSoup(html_text,'lxml')
text_data=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
job=[]
company_name=[]
job_description=[]
key_skills=[]
posted_date=[]

# getting all the required information in the webpage related to job_name,company_name,job_description,key_skills,posted_date
# after getting the required info appending to a list
for text in text_data:
    job.append(text.find('h2').text.replace(' ',''))
    company_name.append(text.find('h3',class_='joblist-comp-name').text.replace(' ',''))
    job_description.append(text.find('ul',class_='list-job-dtl clearfix').text.replace(' ',''))
    key_skills.append(text.find('span',class_='srp-skills').text.replace(' ',''))
    posted_date.append(text.find('span',class_='sim-posted').text)

# here removing all the unwanted characters
job=[i.replace('\n','').replace('\r','') for i in job]
company_name=[i.replace('\n','').replace('\r','') for i in company_name]
job_description=[i.replace('\n','').replace('\r','') for i in job_description]
key_skills=[i.replace('\n','').replace('\r','') for i in key_skills]
posted_date=[i.replace('\n','').replace('\r','').replace('\t','') for i in posted_date]

# passing all the required info to dataframe.After that we are transferring the data to .csv for doing other downstream activities-ML,EDA
df=pd.DataFrame({'job_name':job,
             'company_name':company_name,
            'job_description':job_description,
            'key_skills':key_skills,
            'posted_date':posted_date})
print(df)
df.to_csv('python_jobs_TimesJob_portal.csv')



