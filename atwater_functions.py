import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore


def load_data(stock_file_path, political_file_path):
    """Load and clean stock and political control data"""
    # Load stock data
    stock_data = pd.read_csv(stock_file_path)
    if stock_data.columns[0] == "Unnamed: 0" or stock_data.columns[0] == "":
        stock_data.rename(columns={stock_data.columns[0]: "Date"}, inplace=True)
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])

    # Load political data
    political_data = pd.read_csv(political_file_path)
    political_data['Start Date'] = pd.to_datetime(political_data['Start Date'])
    political_data['End Date'] = pd.to_datetime(political_data['End Date'])

    # Expand political control data to cover all dates in stock data periods
    date_ranges = [
        pd.date_range(start=row['Start Date'], end=row['End Date'], freq='W-FRI')
        for _, row in political_data.iterrows()
    ]

    political_data = political_data.loc[
        political_data.index.repeat([len(rng) for rng in date_ranges])
    ]
    political_data['Date'] = pd.to_datetime(
        [date for rng in date_ranges for date in rng]
    )

    # Select relevant columns
    political_data[['Date', 'President', 'Senate', 'House']]

    return stock_data, political_data


def merge_data(stock_data, political_data):
    """Merge stock data with political data"""
    merge_data = pd.merge(stock_data, political_data, on="Date", how="inner")
    return merge_data

def plot_with_dividers(merged_data, political_file_path):
    """Plot stock with 2-year dividers indicating control periods"""
    # Load political data
    political_data = pd.read_csv(political_file_path)
    political_data['Start Date'] = pd.to_datetime(political_data['Start Date'])
    political_data['End Date'] = pd.to_datetime(political_data['End Date'])


    plt.figure(figsize=(14,8))

    # Plot stock closing price
    sns.lineplot(
        data=merged_data,
        x="Date",
        y="4. close",
        label = "Stock Closing Price"
    )

    # Add vertical lines for control period dividers
    

    # Add labels for each control period

    
    plt.title("Stock Closing Price Over Time with Political Control Periods")
    plt.ylabel("Closing Price")
    plt.xlabel("Date")
    plt.tight_layout()
    plt.show()