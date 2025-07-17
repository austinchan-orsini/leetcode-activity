import requests
import datetime
import os

USERNAME = "speaba"  # your LeetCode username
FILENAME = "solved_problems.txt"

def get_solved_problems():
    url = f"https://leetcode-stats-api.herokuapp.com/{USERNAME}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch LeetCode data")
    data = response.json()
    return data.get("totalSolved", 0)

def append_problem_entry(problem_name):
    date_str = datetime.date.today().isoformat()
    with open(FILENAME, "a") as f:
        f.write(f"{date_str}: {problem_name}\n")

def make_commit(problem_name):
    os.system("git add .")
    os.system(f'git commit -m "Add solved problem: {problem_name}"')

def main():
    # Read last total from file
    last_total = 0
    if os.path.exists("last_total.txt"):
        with open("last_total.txt", "r") as f:
            last_total = int(f.read())

    current_total = get_solved_problems()
    new_problems = current_total - last_total

    if new_problems <= 0:
        print("No new problems solved today.")
        return

    # Simulate problem names (we can’t get real names w/o login)
    for i in range(new_problems):
        problem_name = f"Problem_{current_total - new_problems + i + 1}"
        append_problem_entry(problem_name)
        make_commit(problem_name)

    # Update last_total
    with open("last_total.txt", "w") as f:
        f.write(str(current_total))

if __name__ == "__main__":
    main()
