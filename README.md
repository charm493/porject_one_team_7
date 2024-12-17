![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![edX](https://img.shields.io/badge/edX-%2302262B.svg?style=for-the-badge&logo=edX&logoColor=white)

# project_one_team_7
## Overview
This project analyzes the relationship between stock price vs political control (house, senate, president) in the United States.

## How to get stock data
1. Get api key from [Alpha Vantage](https://www.alphavantage.co/)       
2. Set your environment variable in terminal
> set ALPHA_VANTAGE_API_KEY="your-api-key"
3. (Optional) edit **STOCK_DATA_MAP** and call to **bulk_get_stock_data**
4. Run script
> python data-gather.py

## Files n Folders
:paperclip: create_datasets - the main evaluation of data for this project, including the creation of datasets and visualizations       
:card_index_dividers: raw_data - raw data straight from Alpha Vantage, and political data     
:card_index_dividers: cleaned_data - raw_data combined with political data        
:card_index_dividers: lame_duck - cleaned_data specifically for lame duck periods     
:card_index_dividers: percent_change - percent change data between larger periods of time     
:card_index_dividers: lame_duck_perc_change - percent change data between larger periods of time, specifically during lame duck (duration where successor is already chosen) periods      
