import requests
from bs4 import BeautifulSoup

url = "http://www.cessi.in/coronavirus/pune"

page = requests.get(url)

#print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

data = soup.findAll(attrs= {'class':'btn btn-primary btn-demo'})
# confirm_cases_live = confirm_cases_live[0].text.replace('<h5 class="card-title text-md text-md-lg">' , " ")
print(data)


# recovered_cases_live = soup.findAll(attrs= {'class':'card-title text-md text-md-lg'})
# recovered_cases_live = recovered_cases_live[1].text.replace('<h5 class="card-title text-md text-md-lg">' , " ")
 print(recovered_cases_live)

# death_cases_live = soup.findAll(attrs= {'class':'card-title text-md text-md-lg'})
# death_cases_live = death_cases_live[3].text.replace('<h5 class="card-title text-md text-md-lg">' , " ")
 print(death_cases_live)