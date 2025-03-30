import matplotlib.pyplot as plt
import seaborn as sns

def generate_visualization(df, chart_type="bar", trend="gainers", filename="crypto_chart.png"):
    """
    Generates a visualization based on the specified chart type and trend.
    
    :param df: DataFrame containing cryptocurrency data.
    :param chart_type: Type of chart to generate ('bar' or 'pie').
    :param trend: "gainers" or "losers" to dynamically update the title.
    :param filename: Name of the file to save the visualization.
    """
    if trend == "gainers":
        title = "Top 10 Cryptos with Highest Gains (24h)"
    elif trend == "losers":
        title = "Top 10 Cryptos with Highest Losses (24h)"
    else:
        title = "Crypto Market Trends"

    if chart_type == "bar":
        generate_bar_chart(df, filename, title)
    elif chart_type == "pie":
        generate_pie_chart(df, filename, title)
    else:
        raise ValueError("Invalid chart type. Choose 'bar' or 'pie'.")

def generate_bar_chart(df, filename, title):
    """
    Generates a bar chart of the top 10 cryptocurrencies by price change percentage.
    """
    plt.figure(figsize=(20, 6))
    sns.barplot(x=df["price_change_percentage_24h"], y=df["id"], hue=df["id"], palette="viridis", legend=False)
    plt.xlabel("24h Price Change (%)")
    plt.ylabel("Cryptocurrency")
    plt.title(title)
    plt.grid(axis="x", linestyle="--", alpha=0.7)

    plt.savefig(filename)
    """plt.show()"""

def generate_pie_chart(df, filename, title):
    """
    Generates a pie chart of the top 10 cryptocurrencies by market cap.
    """
    plt.figure(figsize=(8, 8))
    plt.pie(df["market_cap"], labels=df["id"], autopct="%1.1f%%", colors=sns.color_palette("viridis", len(df)))
    plt.title(title)

    plt.savefig(filename)
    """plt.show()"""
