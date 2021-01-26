import csv
import json
import requests

base_url = "https://www.jobplanet.co.kr"
api_url = base_url + "/api/v3/job/search?q="
query = "python"

job_list = list()
def extract_job(job):
    return job['company']

def write_csv(job_list):
    with open('jobs.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for job in job_list:
            writer.writerow(job.items())

def job_planet_scrapper(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        json_data = json.loads(resp.text)
        jobs = json_data['data']['search_result']['jobs']
        next_url = json_data['data']['next_page_url']

        for job in jobs:
            extract_company = extract_job(job)
            job_list.append(extract_company)

        if next_url != "":
            job_planet_scrapper(next_url)

        write_csv(job_list)


if __name__ == '__main__':
    import time
    start = time.time()
    job_planet_scrapper(api_url+query)
    end = time.time()
    print("spend time :", end - start)

