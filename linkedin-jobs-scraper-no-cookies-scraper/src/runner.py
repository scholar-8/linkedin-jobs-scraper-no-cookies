thonimport json
import requests
from extractors.linkedin_parser import LinkedInParser
from outputs.exporters import export_to_json
from config.settings import SETTINGS

def run_scraper():
    # Set up the scraper configuration
    search_params = {
        "keywords": SETTINGS["keywords"],
        "location": SETTINGS["location"],
        "experience_level": SETTINGS["experience_level"],
        "workplace_type": SETTINGS["workplace_type"],
        "easy_apply": SETTINGS["easy_apply"]
    }

    # Fetch job data
    scraper = LinkedInParser(search_params)
    job_listings = scraper.scrape_jobs()

    # Export data to JSON file
    export_to_json(job_listings)

if __name__ == "__main__":
    run_scraper()