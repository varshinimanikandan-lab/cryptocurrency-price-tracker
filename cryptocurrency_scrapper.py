import time
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_crypto_data():
    options = Options()
    options.add_argument("--headless=new")  # modern headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://coinmarketcap.com/")

    wait = WebDriverWait(driver, 15)

    # Wait until the table is present
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))

    # Find top 10 crypto rows
    rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")[:10]

    crypto_data = []
    for row in rows:
        try:
            cols = row.find_elements(By.TAG_NAME, "td")

            name = cols[2].text.split('\n')[0] if len(cols) > 2 else "N/A"
            price = cols[3].text if len(cols) > 3 else "N/A"
            change_24h = cols[4].text if len(cols) > 4 else "N/A"
            market_cap = cols[7].text if len(cols) > 7 else "N/A"

            crypto_data.append({
                "Name": name,
                "Price (USD)": price,
                "24h Change": change_24h,
                "Market Cap": market_cap,
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        except Exception as e:
            print(f"Error reading row: {e}")
            continue

    driver.quit()
    return crypto_data

def save_to_csv(data, filename="crypto_prices.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f" Data saved to {filename}")

def main():
    print("Fetching live cryptocurrency data...\n")
    data = get_crypto_data()
    if data:
        save_to_csv(data)
        print("\nLatest Top 10 Cryptocurrencies:\n")
        print(pd.DataFrame(data))
    else:
        print("⚠️ No data fetched. Please try again later.")

if __name__ == "__main__":
    main()
