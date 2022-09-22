import bs4 as bs
import requests


def get_problem_name(problem_link):
    response = requests.get(problem_link)
    soup = bs.BeautifulSoup(str(response.content), "lxml")
    return soup.find("h2", attrs={"id": "problem-name"}).text


# Open problem_link
def get_problems_by_user(user_id):
    response = requests.get(f"https://www.spoj.com/users/{user_id}/")
    soup = bs.BeautifulSoup(str(response.content), "lxml")
    result = []
    for a in soup.findAll("a"):
        href = a.attrs["href"]
        if len(href) > 11 and "problems" in href:
            problem_link = "https://www.spoj.com" + href
            problem_name = get_problem_name(problem_link)
            result.append((problem_link, problem_name))


problems = get_problems_by_user("khanhvh")
for problem in problems:
    problem[0]  # problem_link
    problem[1]  # problem_name
