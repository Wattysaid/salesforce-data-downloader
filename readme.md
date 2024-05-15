# 📊 Salesforce Data Downloader 📊

Welcome to the **Salesforce Data Downloader** repository! This project allows you to log in to Salesforce, preview data from various Salesforce objects, and download the data as CSV files. The scripts prompt for login details and enable you to interactively select which objects to download.

## 🗂️ Repository Structure


### Files

- `login.py` - Prompts the user for Salesforce login details and creates a session.
- `download_data.py` - Allows the user to select Salesforce objects, preview data, and download it.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `simple-salesforce` library

### Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/salesforce-data-downloader.git
    cd salesforce-data-downloader
    ```

2. **Install Dependencies**:

    ```bash
    pip install simple-salesforce pandas
    ```

## 🛠 Usage

1. **Run `login.py` to Login to Salesforce**:

    Execute the `login.py` script to prompt the user for Salesforce login details and create a session.

    ```bash
    python login.py
    ```

2. **Run `download_data.py` to Select and Download Data**:

    Execute the `download_data.py` script to select an object, view sample data, and download the data.

    ```bash
    python download_data.py
    ```

    Follow the prompts to select the Salesforce object, view sample data, and decide whether to download the full data.

## ⚙️ Functions

### `login.py`

- **`login_to_salesforce()`**: Prompts the user for Salesforce login details and returns a Salesforce session object.

### `download_data.py`

- **`list_salesforce_objects(sf)`**: Retrieves a list of all available Salesforce objects.
- **`get_object_data(sf, object_name)`**: Retrieves sample data from the selected Salesforce object.
- **`download_salesforce_data(sf, object_name)`**: Downloads the full data from the selected Salesforce object and saves it as a CSV file.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


