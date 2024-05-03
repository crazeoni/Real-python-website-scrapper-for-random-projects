import requests
from bs4 import BeautifulSoup
from random import choices



url = "https://realpython.com/tutorials/projects/"
page = requests.get(url)

print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
python_projects = soup.find_all('div', class_="col-12 col-md-6 mb-5")
projects_title = []

for projects in python_projects:
    title = projects.find("h2", class_="card-title")
    level = projects.find("a", class_="badge badge-light text-muted")
    print(title.text)
    print(level.text)
    projects_title.append(title.text + " " + level.text)
projects_title

random_project = choices(projects_title)
random_project
