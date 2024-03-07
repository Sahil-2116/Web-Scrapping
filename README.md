#------Amazon Product Web Scraping Data Analytics Project-----#
This project aims to scrape product data from Amazon using Python's BeautifulSoup library, perform basic data analytics, and store the data in a CSV file for further analysis.

Table of Contents
- Introduction
- Features
- Requirements
- Usage
- Contributing

The project utilizes web scraping techniques to extract product information such as title and price from Amazon's website. 
It then stores this data in a CSV file for further analysis. Additionally, the project includes a function to periodically update the product data.

#---Features---#
Scrapes product title and price from Amazon
Stores scraped data in a CSV file
Periodically updates product data
Requirements

To run this project, you need:

- Python 3.x
- BeautifulSoup library
- Requests library
- Pandas library
You can install the required libraries using pip:

bash
Copy code
pip install beautifulsoup4 requests pandas
Usage
Clone this repository:
bash
Copy code
git clone https://github.com/your-username/amazon-product-scraper.git
Navigate to the project directory:
bash
Copy code
cd amazon-product-scraper
Run the Python script:
bash
Copy code
python scraper.py
The script will scrape the product data from Amazon and store it in a CSV file named AmazonWebScraperDataset.csv.

Contributing
Contributions are welcome! If you want to contribute to this project, feel free to open an issue or submit a pull request.
