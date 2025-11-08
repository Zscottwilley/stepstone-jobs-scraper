thonimport requests
from bs4 import BeautifulSoup

class StepStoneParser:
    def __init__(self, settings):
        self.settings = settings
        self.base_url = "https://www.stepstone.de"

    def scrape_job_listings(self):
        job_listings = []
        for search_url in self.settings['search_urls']:
            page_number = 1
            while True:
                url = f"{search_url}?page={page_number}"
                response = requests.get(url)
                if response.status_code != 200:
                    break

                soup = BeautifulSoup(response.content, 'html.parser')
                jobs = self._parse_job_listings(soup)

                if not jobs:
                    break

                job_listings.extend(jobs)
                page_number += 1

        return job_listings

    def _parse_job_listings(self, soup):
        jobs = []
        job_elements = soup.find_all('div', class_='job-element')
        for job_element in job_elements:
            job = self._parse_job(job_element)
            jobs.append(job)

        return jobs

    def _parse_job(self, job_element):
        job_id = job_element['data-job-id']
        title = job_element.find('a', class_='job-title').get_text(strip=True)
        company_name = job_element.find('div', class_='company').get_text(strip=True)
        company_url = job_element.find('a', class_='company-link')['href']
        date_posted = job_element.find('div', class_='date-posted').get_text(strip=True)
        location = job_element.find('div', class_='location').get_text(strip=True)
        salary = job_element.find('div', class_='salary').get_text(strip=True) if job_element.find('div', class_='salary') else ''
        work_from_home = job_element.find('div', class_='work-from-home').get_text(strip=True)
        job_description = job_element.find('div', class_='job-description').get_text(strip=True)

        return {
            'id': job_id,
            'title': title,
            'companyName': company_name,
            'companyUrl': company_url,
            'companyLogoUrl': '',
            'datePosted': date_posted,
            'location': location,
            'salary': salary,
            'workFromHome': work_from_home,
            'jobDescription': job_description
        }