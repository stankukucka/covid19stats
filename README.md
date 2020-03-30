# Covid 19 stats 
This is a Scrapy project to scrape data from the Worldometers page related to the Covid-19 Coronavirus pandemic page from https://www.worldometers.info/coronavirus/ (GitHub repo).

This project is meant for helping to set up regular crawling purposes.

## How to run spider
Activate your Virtual Env:

    $ source scrapy_env/bin/activate

Enter directory: 
    
    $ cd covid19stats

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl covid19stats
    
Or specify output file you would like to save to your crawled data

    $ scrapy crawl covid19 -o covid19.csv

## Deploy script to Cloud service
Create scrapinghub service [Cloudera](https://scrapinghub.com/?rfsn=3908921.3359b4)
And deploy via shub command. You can read all [tutorial here](https://support.scrapinghub.com/support/solutions/articles/22000204081-deploying-your-spiders-to-scrapy-cloud)
