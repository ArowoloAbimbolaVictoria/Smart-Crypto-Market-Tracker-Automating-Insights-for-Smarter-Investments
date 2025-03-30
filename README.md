# Smart-Crypto-Market-Tracker-Automating-Insights-for-Smarter-Investments
A Python Project That Tracks Market Trends and Sends Daily Reports
# Crypto Data insights

## Overview
This Python script fetches real-time cryptocurrency data from the CoinGecko API. It identifies the top 10 cryptocurrencies to buy (highest gainers) and the top 10 to sell (highest losers) based on the last 24-hour price change percentage.It generates visualizations, and sends email reports daily to a list of recipients at a scheduled time.


##  Features
- **Fetch Live Crypto Data**: Automatically retrieves the latest cryptocurrency market data in csv.
- **Analyze Market Trends**: Identifies the **top 10 gainers** and **top 10 losers** in the market.
- **Generate Visual Reports**: Creates bar chart visualizations for both gainers and losers.
- **Automated Email Reports**: Sends visual reports to recipients via email.

##  How It Works
1. **Fetches Data**: Retrieves the latest crypto data using `dataHandler`.
2. **Processes Top Movers**: Identifies the top gainers and losers.
3. **Creates Visualizations**: Generates bar charts for market trends.
4. **Sends Email Reports**: Emails the visualizations to recipients.

##  Project Structure
```
📦 crypto-market-visualizer
├── dataHandler.py        # Handles data fetching and processing
├── visualizationHandler.py # Generates visual reports
├── personnelHandler.py   # Manages recipient email list
├── emailHandler.py       # Sends emails with visual reports
├── application.py        # Main script to execute the process
├── Personnel.csv         # List of email recipients
└── README.md             # Documentation
```

##  Setup & Installation
### 1️ Prerequisites
Ensure you have **Python 3.x** installed, along with the required libraries:

```sh
pip install pandas matplotlib requests smtplib email
```

### 2️ Clone the Repository
```sh
git clone https://github.com/your-username/crypto-market-visualizer.git
cd crypto-market-visualizer
```

### 3️ Configure Email Settings
Edit `emailHandler.py` and update the SMTP settings with your email credentials.

```python
SMTP_SERVER = "smtp.your-email.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your-email@example.com"
EMAIL_PASSWORD = "your-password"
```

### 4️ Run the Application
Execute the main script to fetch data, generate visualizations, and send emails.
```sh
python application.py
```

## 📧 Email Report Example
Your email recipients will receive a message like this:
```
Subject: Today's Crypto Trends Are In!

Hello [Recipient Name],

Get the latest insights on the market’s top gainers and losers with a quick snapshot of today’s trends. 

Attached are the latest crypto market visualizations (Top Gainers & Top Losers).

Best,
Your Automated Crypto Bot 🤖
```

##  Customization
- Modify `dataHandler.py` to change data sources.
- Adjust `visualizationHandler.py` for different chart styles.
- Edit `Personnel.csv` to update email recipients.

##  Contributing
Pull requests are welcome! Feel free to open an issue or suggest improvements.

---
 **Stay ahead in the crypto market with automated insights!**

