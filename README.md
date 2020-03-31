# Covid 19 stats 
This is a Scrapy project to scrape data from the Worldometers page related to the Covid-19 Coronavirus pandemic page at https://www.worldometers.info/coronavirus/.

This project is meant for helping to set up regular crawling purposes.

## How to run spider
Activate your Virtual Env:

    $ source scrapy_env/bin/activate

Enter directory: 
    
    $ cd covid19stats

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl covid19stats
    
If you want to save the scraped data to a file, you can pass the `-o` option to save data as CSV file:

    $ scrapy crawl covid19 -o covid19.csv
    
Or save data as a JSON file:

    $ scrapy crawl covid19 -o covid19.json

## Deploy script to Cloud service
Create scrapinghub service [Cloudera](https://scrapinghub.com/?rfsn=3908921.3359b4). Deploy via shub command. You can read all [tutorial here](https://support.scrapinghub.com/support/solutions/articles/22000204081-deploying-your-spiders-to-scrapy-cloud)
