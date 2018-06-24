from xmljson import parker    
from json import dumps
import argparse
from xml.etree.ElementTree import fromstring
# TODO: Use multiprocessing package to spawning multiple process_folder
from multiprocessing import Pool
from multiprocessing import Process

parser = argparse.ArgumentParser(description='Convert XML to JSON')
parser.add_argument('-i', '--input_xml_folder', help='Path to the XML folder', default='./xml')
parser.add_argument('-o', '--output_json_folder', help='Path to the JSON folder', default='./json')
parser.add_argument('-max', '--max_threads', default=60)
args = parser.parse_args()

# TODO: Use this variable to run multiple threads of 'transform_xml_to_json'
MAX_THREADS = int(args.max_threads)


def transform_xml_to_json(xml_file_input, json_file_output):
    """Transform Single File"""
    with open(xml_file_input,'r') as f1:
        xml_text=f1.read()
    with open(json_file_output,'w') as f2:
        json_text=dumps(parker.data(fromstring((xml_text))))
        f2.write(json_text)


def process_folder(xml_folder, json_folder):
    """For each file in xml_folder call transform_xml_to_json and
    Create JSON file in json_folder"""
    # TODO: To complete


if __name__ == "__main__":
    # TODO: Write a code to run transform_xml_to_json in multiple threads for different folders.
    # This code should read the structure of input_xml_folder and replicate the structure in json_output_folder
    # The code should use multiprocessing to spawn a threat for each sub folder up to MAX_THREADS
    #

    print('done')