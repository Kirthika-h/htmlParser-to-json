from bs4 import BeautifulSoup
import json
with open('index.html','r') as html_file:
    html_content=html_file.read()
soup=BeautifulSoup(html_content,'html.parser')
data_list=[]
for li_tag in soup.find_all('li'):
    capital=li_tag.find('strong').get_text(strip=True)
    state=li_tag.find('span').get_text(strip=True)

    data_list.append({

        'capital':capital,
        'state':state
        
    })
json_data={"capitals":data_list,"summary":{"numberOfCapitals":len(data_list)}}
json_output=json.dumps(json_data,indent=2)
with open('results.json','w') as json_file:
    json_file.write(json_output)
print("JSON data has been written to 'results.json'.")