import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

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

        # Create a pandas DataFrame from the extracted data
        df = pd.DataFrame(data)
        # df = df.apply(lambda x: " ".join(x.str.translate(str.maketrans('', '', "\t\n\r\x0b\x0c"))).split() if x.dtype == "object" else x)
        # df = df.apply(lambda x: " ".join(x.split()) if x.dtype == "object" else x)

        # # Print the DataFrame
        # print(tabulate(df_trimmed))
        
        new_rows = []
        for index, row in df.iterrows():
            if index % 2 == 1:  # Check if index is odd
                for i in row:
                    if type(i) == str:
                        i = " ".join(i.split())
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

        return pd.DataFrame(new_rows)

    else:
        print("Failed to retrieve webpage:", response.status_code)
        return -1
    
ac = pd.DataFrame(columns=["scenario-text", "scenario-id", "procedure", "adult-rrl", "peds-rrl", "appropriateness", "empty-1", "empty-2"], dtype="object")

scenario_list = [
                    "https://gravitas.acr.org/ACPortal/GetDataForOneScenario?senarioId=5564",
                    "https://gravitas.acr.org/ACPortal/GetDataForOneScenario?senarioId=5568"
]

for url in scenario_list:
    new_ac = get_criteria_for_scenario(url)
    new_ac.columns = ac.columns
    ac = pd.concat([ac, new_ac], ignore_index=True)

ac = ac.drop(['empty-1', 'empty-2'], axis=1)
ac.to_csv("output.csv")

