import dataHandler
import visualizationHandler
import personnelHandler
import emailHandler

PERSONNEL_FILE = "Personnel.csv"

def main():
    # Step 1: Fetch crypto data
    data_filename = dataHandler.fetch_crypto_data()
    if not data_filename:
        return

    # Step 2: Load latest data
    df = dataHandler.load_latest_data()

    # Step 3: Select top 10 gainers and losers
    gainers_df, _ = dataHandler.get_top_cryptos(df, "gainers")
    losers_df, _ = dataHandler.get_top_cryptos(df, "losers")

    # Step 4: Generate visualizations for both
    gainers_visualization_filename = "top_gainers_10.png"
    losers_visualization_filename = "top_losers_10.png"

    visualizationHandler.generate_visualization(gainers_df, chart_type="bar", trend="gainers", filename=gainers_visualization_filename)
    visualizationHandler.generate_visualization(losers_df, chart_type="bar", trend="losers", filename=losers_visualization_filename)

    # Step 5: Load personnel data
    personnel_list = personnelHandler.read_personnel(PERSONNEL_FILE)

    # Step 6: Send emails with both attachments
    emailHandler.send_bulk_emails(personnel_list, [gainers_visualization_filename, losers_visualization_filename])

if __name__ == "__main__":
    main()
