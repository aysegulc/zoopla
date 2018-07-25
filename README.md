
Zoopla Real Estate Agents Scraping Project
-------------------------

This scrapy project is built to extract contact details of real estate agents from zoopla.

Scrapy takes a list of zipcodes as an argument and search agents for each zipcodes, scrape search result pages and agent details.

Scraped items can be saved as json or csv files.


```bash
# Save items to csv file
scrapy crawl zoopla -o zoopla_agents.csv -a zipcode='EC1,EC4'
# save items to json file
scrapy crawl zoopla -o zoopla_agents.json -a zipcode='EC1,EC4'
```
