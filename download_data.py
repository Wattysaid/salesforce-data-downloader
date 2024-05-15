# download_data.py

from login import login_to_salesforce
import pandas as pd

def list_salesforce_objects(sf):
    # Retrieve metadata about all objects
    object_descriptions = sf.describe()
    object_names = [obj['name'] for obj in object_descriptions['sobjects']]
    return object_names

def get_object_data(sf, object_name):
    # Fetch data from the specified Salesforce object
    query = f"SELECT * FROM {object_name} LIMIT 10"
    try:
        data = sf.query_all(query)
        records = data['records']
        df = pd.DataFrame(records)
        if 'attributes' in df.columns:
            df.drop(columns='attributes', inplace=True)
        return df
    except Exception as e:
        print(f"Error fetching data for object {object_name}: {e}")
        return None

def download_salesforce_data(sf, object_name):
    # Fetch all data from the specified Salesforce object
    query = f"SELECT * FROM {object_name}"
    try:
        data = sf.query_all(query)
        records = data['records']
        df = pd.DataFrame(records)
        if 'attributes' in df.columns:
            df.drop(columns='attributes', inplace=True)

        # Save to CSV
        file_name = f"{object_name}_data.csv"
        df.to_csv(file_name, index=False)
        print(f"Data downloaded successfully and saved to {file_name}")
    except Exception as e:
        print(f"Error downloading data: {e}")

if __name__ == "__main__":
    sf = login_to_salesforce()
    if sf:
        objects = list_salesforce_objects(sf)
        print("Available Salesforce objects:")
        for i, obj in enumerate(objects, 1):
            print(f"{i}. {obj}")

        object_index = int(input("Enter the number of the object you want to download: ")) - 1
        if 0 <= object_index < len(objects):
            selected_object = objects[object_index]
            print(f"You selected: {selected_object}")

            print("Fetching sample data...")
            sample_data = get_object_data(sf, selected_object)
            if sample_data is not None:
                print("Sample data from the selected object:")
                print(sample_data.head())

                download = input("Do you want to download the full data for this object? (yes/no): ").strip().lower()
                if download == 'yes':
                    download_salesforce_data(sf, selected_object)
                else:
                    print("Download cancelled.")
            else:
                print("Failed to retrieve sample data.")
        else:
            print("Invalid selection.")
