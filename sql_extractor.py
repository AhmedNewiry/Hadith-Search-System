import gzip


def extract_sql_file(input_file_path, output_file_path):
    """Extracts a .sql.gz file to .sql format."""
    with gzip.open(input_file_path, 'rb') as f_in:
        with open(output_file_path, 'wb') as f_out:
            f_out.write(f_in.read())
    print("Extraction complete.")


def preview_sql_file(file_path, lines=20):
    """Prints a preview of the SQL file."""
    with open(file_path, 'r') as file:
        for _ in range(lines):
            print(file.readline())


if __name__ == "__main__":
    input_file = 'HadithTable.sql.gz'  # Update with your file
    output_file = 'HadithTable.sql'

    extract_sql_file(input_file, output_file)
    preview_sql_file(output_file)
