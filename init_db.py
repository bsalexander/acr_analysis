
import sqlite3
import os
import csv

# Initialize database
def init_db():
    # Create database if it doesn't exist
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'acr_analysis.db')
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Read schema.sql file
        with open('schema.sql', 'r') as f:
            schema = f.read()
        
        # Execute SQL commands from schema file
        cursor.executescript(schema)
        
        # Commit changes
        conn.commit()
        print("Database initialized successfully.")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
        
    finally:
        # Close connection
        cursor.close()
        conn.close()

if __name__ == '__main__':
    init_db()

def init_data():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'acr_analysis.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        # Initialize voters table from CSV
        with open('voters.csv', 'r') as f:
            # next(csv.DictReader(f))  # Skip header row
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                cursor.execute('''
                    INSERT INTO voters (net_id, email, first_name, last_name, pgyear)
                    VALUES (?, ?, ?, ?, ?)
                ''', (row['net_id'], row['email'], row['first_name'], row['last_name'], row['pgyear']))
        
        # Initialize scenarios table from CSV
        with open('acr_ac_scenarios.csv', 'r', encoding="utf-8-sig") as f:
            # next(csv.DictReader(f))  # Skip header row
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                cursor.execute('''
                    INSERT INTO scenarios (panel, scenario_id, scenario_text, scenario_url, sex, age, body_area, priority_clinical_areas)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (row['panel'], row['scenario-id'], row['scenario-text'], row['scenario-url'], row['sex'], row['age'], row['body-area'], row['priority-clinical-areas']))
        
        conn.commit()
        print("Initial data loaded successfully.")
        
    except Exception as e:
        print(f"Error loading initial data: {e}")
        
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    init_db()
    init_data()
