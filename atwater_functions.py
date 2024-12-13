import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
from datetime import timedelta

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


def calculate_election_period_prices(input_df, output_csv_path):
    """
    Process election period energy data to calculate start and end prices, 
    percent change, and other associated details.

    Parameters:
        dataframe (pd.DataFrame): Input DataFrame containing election period energy data.
        output_csv_path (str): File path to save the resulting CSV.

    Returns:
        pd.DataFrame: Processed DataFrame with calculated percent changes and renamed columns.
    """
    # Group data and calculate aggregate metrics
    output_df = (
        input_df.groupby(['Start Date', 'End Date'])
        .agg(
            start_price=('Close', 'last'),
            start_ticker=('Date', 'last'),
            end_price=('Close', 'first'),
            end_ticker=('Date', 'first'),
            President=('President', 'first'),
            House=('House', 'first'),
            Senate=('Senate', 'first'),
            Sector=('Sector', 'first'),
        )
        .reset_index()
    )

    # Calculate percent change from earliest to latest close price
    output_df['Percent Change'] = (
        (output_df['end_price'] - output_df['start_price'])
        / output_df['start_price']
    ) * 100

    # Rename columns for better readability
    output_df = output_df.rename(
        columns={
            'start_price': 'Start Price',
            'end_price': 'End Price',
            'Start Date': 'Start of Term',
            'End Date': 'End of Term'
        }
    )

    # Save to CSV
    output_df.to_csv(output_csv_path, index=False)

    return output_df

def generate_lame_duck_dataset(input_df, output_csv_path):

    # Generate Lame Duck data

    # Convert the 'End Date' column to datetime if not already done
    input_df['End Date'] = pd.to_datetime(input_df['End Date'])
    input_df['Date'] = pd.to_datetime(input_df['Date'])

    # Generate the lame_duck_energy DataFrame based on the new logic
    output_df = pd.concat(
        [input_df[(input_df['Date'] >= end_date - timedelta(days=70)) & (input_df['Date'] <= end_date)] for end_date in input_df['End Date'].unique()])

    # Remove duplicates if any were introduced
    output_df = output_df.drop_duplicates()

    # Save to CSV
    output_df.to_csv(output_csv_path, index=False)

    return output_df

    


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