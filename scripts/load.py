import logging

def load_data(data, output_file):
    logging.info(f"Loading data to {output_file}...")
    data.to_csv(output_file, index=False)
    logging.info("Data loading completed.")
