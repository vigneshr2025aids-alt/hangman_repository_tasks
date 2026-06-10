
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 400,
    "AMZN": 175
}

def main():
    print("--- 📈 Welcome to the Stock Portfolio Tracker 📈 ---")
    print("Available stocks and their prices:")
    for stock, price in STOCK_PRICES.items():
        print(f"- {stock}: ${price}")
    print("-" * 50)

    portfolio = {}
    total_investment = 0

    while True:
        ticker = input("\nEnter the stock ticker you own (or type 'done' to calculate): ").upper()
        
        if ticker == "DONE":
            break
        
        
        if ticker not in STOCK_PRICES:
            print("❌ Stock ticker not found. Please choose from the list above.")
            continue

        
        try:
            quantity = int(input(f"How many shares of {ticker} do you own? "))
            if quantity < 0:
                print("❌ Quantity cannot be negative.")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")
            continue

  
        if ticker in portfolio:
            portfolio[ticker] += quantity
        else:
            portfolio[ticker] = quantity

    
    print("\n" + "=" * 15 + " PORTFOLIO SUMMARY " + "=" * 15)
    
    summary_lines = [] 

    for ticker, qty in portfolio.items():
        price = STOCK_PRICES[ticker]
        item_total = qty * price
        total_investment += item_total
        
        line = f"{ticker}: {qty} shares @ ${price} each = ${item_total}"
        print(line)
        summary_lines.append(line)

    grand_total_line = f"\nTotal Portfolio Value: ${total_investment}"
    print(grand_total_line)
    summary_lines.append(grand_total_line)
    print("=" * 49)

    
    save_choice = input("\nWould you like to save this summary to a text file? (yes/no): ").lower()
    if save_choice in ['yes', 'y']:
        with open("portfolio_summary.txt", "w") as file:
            file.write("STOCK PORTFOLIO TRACKER REPORT\n")
            file.write("-" * 30 + "\n")
            for line in summary_lines:
                file.write(line + "\n")
        print("💾 Summary saved successfully to 'portfolio_summary.txt'!")

if __name__ == "__main__":
    main()