from scripts.log import setup_logging
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data
import logging


def main():
    # Set up logging
    setup_logging()

    folder_path = './data'  # Path to the folder containing source files
    output_file = './output/transformed_data.csv'

    try:
        logging.info("ETL process started.")
        raw_data = extract_data(folder_path)
        transformed_data = transform_data(raw_data)
        load_data(transformed_data, output_file)
        logging.info("ETL process completed successfully.")
    except Exception as e:
        logging.error(f"ETL process failed: {e}")

if __name__ == '__main__':
    main()
