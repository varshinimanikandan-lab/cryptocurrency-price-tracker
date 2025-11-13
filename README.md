Cryptocurrency Price Tracker:

A simple Python project that tracks live cryptocurrency prices using web scraping and automation tools. This project fetches real-time data of popular cryptocurrencies and displays them neatly in a CSV file or console output.
Features

Features:
  fetches live cryptocurrency prices from reliable sources

  Stores the data in a CSV file for easy access

  Uses Selenium and Pandas for automation and data handling

  Automatically updates data at regular intervals

  Handles errors with try-except blocks

Technologies Used:

  Python 3

  Selenium

  Pandas

  Datetime

  WebDriver Manager

How It Works:

  The program launches a browser using Selenium.

  It navigates to a cryptocurrency listing website (e.g., CoinMarketCap).

  Extracts cryptocurrency names, prices, and symbols.

  Saves the results in a crypto_prices.csv file.

Installation:

 Clone this repository:

  git clone https://github.com/<your-username>/cryptocurrency-price-tracker.git


 Navigate to the project directory:

  cd cryptocurrency-price-tracker


 Install the required dependencies:

  pip install -r requirements.txt

Usage:

Run the script:

python cryptocurrency_scrapper.py


After running, you’ll see a file named crypto_prices.csv in your project folder containing live data.

Example Output
Name	Symbol	Price (USD)	Time Fetched
Bitcoin	BTC	$65,423.17	2025-11-13 18:10:32
Ethereum	ETH	$3,412.85	2025-11-13 18:10:32
Dogecoin	DOGE	$0.089	2025-11-13 18:10:32
Project Structure
cryptocurrency-price-tracker
 ┣ 📄 crypto_tracker.py
 ┣ 📄 requirements.txt
 ┣ 📄 crypto_prices.csv
 ┗ 📄 README.md

Troubleshooting

If you encounter issues with Selenium or the browser driver:

Update your Chrome browser.

Run:

pip install -U selenium webdriver-manager

 Future Enhancements

Add real-time graph visualization

Create a GUI dashboard

Integrate with APIs instead of web scraping

 Author:

Varshini M
Individual Project – Cryptocurrency Price Tracker

License:

This project is open-source and available under the MIT License.
