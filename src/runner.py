thonimport json
from extractors.stepstone_parser import StepStoneParser
from outputs.exporters import JsonExporter
from config.settings import Settings

def run_scraper():
    # Load configuration
    settings = Settings.load()

    # Initialize scraper and exporter
    parser = StepStoneParser(settings)
    exporter = JsonExporter(settings['output_file'])

    # Scrape job listings
    job_listings = parser.scrape_job_listings()

    # Export the data
    exporter.export(job_listings)

if __name__ == '__main__':
    run_scraper()