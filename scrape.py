import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import time
from datetime import datetime


def get_criteria_for_scenario(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the table on the page
        table = soup.find("table")  # You might need to adjust this based on the HTML structure

        # Extract the table data
        data = []
        for row in table.find_all("tr"):
            row_data = []
            for cell in row.find_all("td"):
                row_data.append(cell.text)
            data.append(row_data)

        df = pd.DataFrame(data)
        
        new_rows = []
        for index, row in df.iterrows():
            if index % 2 == 1:  # Check if index is odd
                for idx, i in enumerate(row):
                    if type(i) == str:
                        i = " ".join(i.split())
                        row[idx] = i
                if index == 1:
                    txt = row[0]
                    id = row[1]
                    row[3] = row[5]
                    row[4] = row[6]
                    row[5] = row[7]
                else:
                    row[0] = txt
                    row[1] = id
                new_rows.append(row.values)

        return new_rows

    else:
        print("Failed to retrieve webpage:", response.status_code)
        return -1

# main
 

scenarios = pd.read_csv("data/acr_ac_scenarios.csv")
scenario_list = scenarios[scenarios['panel'] == 'Gastrointestinal']['scenario-url'].tolist()

ac = pd.DataFrame(columns=["scenario-text", "scenario-id", "procedure", "adult-rrl", "peds-rrl", "appropriateness", "empty-1", "empty-2"], dtype="object")

total_urls = len(scenario_list)
# Get both url and panel information
scenario_data = scenarios[scenarios['panel'] == 'Gastrointestinal'][['url', 'panel']].values.tolist()

# Update DataFrame columns to include panel
ac = pd.DataFrame(columns=["panel", "scenario-text", "scenario-id", "procedure", "adult-rrl", "peds-rrl", "appropriateness", "empty-1", "empty-2"], dtype="object")

for idx, (url, panel) in enumerate(scenario_data, 1):
    print(f"Processing {idx}/{total_urls}: {url}", end='\r', flush=True)
    new_ac = get_criteria_for_scenario(url)
    if new_ac == -1:
        print(f"\nFailed to retrieve url {url}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('error_log.txt', 'a') as error_file:
            error_file.write(f"[{timestamp}] Failed to retrieve: {url}\n")
    else:
        # Add panel column to each row
        new_ac_with_panel = [[panel] + list(row) for row in new_ac]
        ac = pd.concat([ac, pd.DataFrame(new_ac_with_panel, columns=ac.columns)], ignore_index=True)
    time.sleep(10)  # Pause for 10 seconds between requests    
ac = ac.drop(['empty-1', 'empty-2'], axis=1)
ac.to_csv("output.csv")

