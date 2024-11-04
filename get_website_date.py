from htmldate import find_date

# url = "https://uca.edu/politicalscience/home/research-projects/dadm-project/asiapacific-region/nepal-1923-present/"
url = "https://itihasaa.com/ranas/mohan-shumsher/"
url = "https://myrepublica.nagariknetwork.com/news/reassessing-panchayat/"

found_date = find_date(url)

if found_date:
    from datetime import datetime

    dt = datetime.strptime(found_date, "%Y-%m-%d")
    print(f"year: {dt.year}")
    print(f"month: {dt.strftime('%B')}")
    print(f"day: {dt.day}")
else:
    print("No date found")

# print(found_date)
