
import pandas as pd
import json
import logging
import os
import xml.etree.ElementTree as ET


def extract_csv(file_path):
    return pd.read_csv(file_path)

def extract_json(file_path):
    with open(file_path, 'r') as json_file:
        return pd.DataFrame([json.loads(line) for line in json_file])

def extract_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    xml_data = []
    for person in root.findall('person'):
        xml_data.append({
            'name': person.find('name').text,
            'height': float(person.find('height').text),
            'weight': float(person.find('weight').text)
        })

def extract_data(folder_path):
    logging.info("Starting data extraction...")
    combined_data = []
    
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        try:
            if file_name.endswith('.csv'):
                combined_data.append(extract_csv(file_path))
            elif file_name.endswith('.json'):
                combined_data.append(extract_json(file_path))
            elif file_name.endswith('.xml'):
                combined_data.append(extract_xml(file_path))
            logging.info(f"Extracted data from {file_name}.")
        except Exception as e:
            logging.error(f"Failed to extract data from {file_name}: {e}")

    logging.info("Data extraction completed.")
    return pd.concat(combined_data, ignore_index=True)