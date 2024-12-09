import csv


def extract_hadith_data(file_path, table_name="HadithTable"):
    """Extract INSERT statements for the HadithTable."""
    hadith_data = []
    with open(file_path, 'r') as file:
        for line in file:
            if f"INSERT INTO `{table_name}`" in line:
                hadith_data.append(line)
    return hadith_data


def filter_tirmidhi_data(hadith_data):
    """Filters rows for the Tirmidhi book."""
    return [row for row in hadith_data if 'Tirmidhi' in row]


def save_to_csv(data, output_csv, columns):
    """Saves the filtered data to a CSV file."""
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(columns)  # Adjust columns as needed
        for row in data:
            writer.writerow(row)
    print("CSV export complete.")


if __name__ == "__main__":
    input_sql = 'HadithTable.sql'
    output_csv = 'Tirmidhi.csv'

    hadith_data = extract_hadith_data(input_sql)
    tirmidhi_data = filter_tirmidhi_data(hadith_data)

    # Replace with the actual column names from your database schema
    save_to_csv(tirmidhi_data, output_csv, columns=['Column1', 'Column2', 'Column3'])
