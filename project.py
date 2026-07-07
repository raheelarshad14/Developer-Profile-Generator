import requests
import json
from datetime import datetime

BASE_URL = "https://api.github.com/users/"

def get_user(username):
    user_url = BASE_URL + username

    response = requests.get(user_url)

    if response.status_code != 200:
        raise ValueError("GitHub user not found.")

    return response.json()


def get_repos(username):
    repo_url = BASE_URL + username + "/repos"
    response = requests.get(repo_url)

    if response.status_code != 200:
        return []
    return response.json()


def language_stats(repositories):
    languages = {}

    for repo in repositories:
        language = repo["language"]

        if language is None:
            continue

        if language in languages:
            languages[language] += 1
        else:
            languages[language] = 1

    return languages


def total_stars(repositories):

    stars = 0

    for repo in repositories:
        stars += repo["stargazers_count"]

    return stars


def top_projects(repositories):
    sorted_repos = sorted(
        repositories,
        key = lambda x: x["stargazers_count"],
        reverse = True
    )
    return sorted_repos[:5]

""" About Key and Lambda functions:
    -> key asks for a function which extracts the value python should use for sorting
    -> we provide that function through lambda definition in my example x can be anything,
    -> the goal is to just give a blueprint of the function,
    -> lambda definition is handy when we need to use the function only once in our program
    -> lambda x(argument-dict in this case): x(dict)["stargazers_count(key)"] """

def write_to_json(report):
    with open("Resume.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent = 4, ensure_ascii = False)

def write_to_md(report):
    with open("Resume.md", "w", encoding="utf-8") as file:
        file.write(f"# {report['name']}\n\n")

        file.write(f"Username: **{report['username']}**\n\n")

        file.write(f"Followers: {report['followers']}\n\n")

        file.write(f"Following: {report['following']}\n\n")

        file.write(f"Public Repositories: {report['repositories']}\n\n")

        file.write(f"Total Stars: {report['stars']}\n\n")

        file.write("## Languages\n\n")

        for language, count in sorted(report["languages"].items(), key = lambda x: x[1], reverse = True):
            file.write(f"- {language}: {count}\n\n")

        file.write("## Top Projects\n\n")

        for project in report["top_projects"]:
            file.write(f"- {project['name']}: (Stars: {project['stargazers_count']})\n\n")


def main():
    username = input("Enter GitHub username: ")

    try:
        user = get_user(username)
        repos = get_repos(username)

    except ValueError as e:
        print(e)
        return

    languages = language_stats(repos)
    stars = total_stars(repos)
    top = top_projects(repos)


    #List comprehension - getting only the required elements from the list

    top_projects_list = []

    for repo in top:
        project = {
        "name": repo["name"],
        "stargazers_count": repo["stargazers_count"],
        }
        top_projects_list.append(project)


    report = {
        "name": user["name"] or "Not Provided",

        "username": user["login"],

        "followers": user["followers"],

        "following": user["following"],

        "repositories": len(repos),

        "stars": stars,

        "languages": languages,

        "top_projects": top_projects_list,

        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    write_to_json(report)
    write_to_md(report)

    #Terminal response
    print("\n==============================")
    print("Developer Profile")
    print("==============================")

    print(f"Name: {report['name']}")
    print(f"Username: {report['username']}")
    print(f"Followers: {report['followers']}")
    print(f"Following: {report['following']}")
    print(f"Repositories: {report['repositories']}")
    print(f"Total Stars: {report['stars']}")

    print("\nLanguages:")

    for language, count in sorted(
            languages.items(),
            key=lambda item: item[1],
            reverse=True
    ):
        print(f"{language}: {count}")

    print("\nTop Projects:")

    for project in report["top_projects"]:
        print(
            f"{project['name']} (Stars: {project['stargazers_count']})"
        )

    print("\nGenerated Files:")
    print("resume.json")
    print("resume.md")


if __name__ == "__main__":
    main()



