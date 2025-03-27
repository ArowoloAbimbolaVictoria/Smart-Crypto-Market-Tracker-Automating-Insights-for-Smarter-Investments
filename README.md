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

## Code Snippets
### Fetching Crypto Data
```python
import requests
import pandas as pd
from datetime import datetime

# API details
url = 'https://api.coingecko.com/api/v3/coins/markets'
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 250,
    'page': 1
}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv('crypto_data.csv', index=False)
    print("Data saved successfully!")
else:
    print(f"Error: {response.status_code}")
```

### Sending Email
```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email.encoders

def send_mail(subject, body, filename):
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    receiver_email = "recipient_email@gmail.com"
    
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    
    with open(filename, 'rb') as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        email.encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={filename}')
        message.attach(part)
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
```

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

