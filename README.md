# Smart-Crypto-Market-Tracker-Automating-Insights-for-Smarter-Investments
A Python Project That Tracks Market Trends and Sends Daily Reports
# Crypto Data Fetcher

## Overview
This Python script fetches real-time cryptocurrency data from the CoinGecko API. It identifies the top 10 cryptocurrencies to buy (highest gainers) and the top 10 to sell (highest losers) based on the last 24-hour price change percentage. The data is saved in CSV format and emailed daily at a scheduled time.

## Features
- Fetches real-time cryptocurrency data from CoinGecko API.
- Saves the complete dataset as a CSV file.
- Identifies the top 10 cryptocurrencies with the highest price increase.
- Identifies the top 10 cryptocurrencies with the highest price decrease.
- Sends an email report with the dataset attached.
- Runs automatically every day at 8 AM.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install requests pandas schedule smtplib email
```

## How It Works
### 1. Fetching Data
The script queries the CoinGecko API for the top 250 cryptocurrencies based on market cap. It extracts relevant fields such as:
- `id`
- `current_price`
- `market_cap`
- `price_change_percentage_24h`
- `all-time high (ath)`
- `all-time low (atl)`

### 2. Processing Data
- The script identifies the top 10 gainers and losers based on the 24-hour price change percentage.
- The complete dataset is saved in a CSV file.
- Separate CSV files are created for the top 10 gainers and top 10 losers.

### 3. Sending Email
- An email is sent to the user with a summary of the top gainers and losers.
- The CSV file is attached to the email.

### 4. Scheduling
- The script is scheduled to run daily at 8 AM using the `schedule` library.

## Setup Instructions
1. **Update Email Credentials**
   Modify the `send_mail` function with your sender email and password.

2. **Run the script**
   ```bash
   python crypto_data_fetcher.py
   ```

3. **Automate Execution**
   - To run it automatically every day, consider setting up a cron job (Linux/macOS) or Task Scheduler (Windows).


## Troubleshooting
- **Invalid Credentials**: Ensure that you enable "Less secure apps" access for your email.
- **API Limitations**: The CoinGecko API has rate limits; ensure you are not exceeding them.
- **Email Not Sent**: Check SMTP settings and credentials.

## Future Improvements
- Integrate a database for historical tracking.
- Implement Telegram or WhatsApp alerts.
- Add more filtering options.

## License
This project is open-source and available.

---

Enjoy automated crypto insights! 

