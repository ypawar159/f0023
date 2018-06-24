import os
from xmljson import parker
from json import dumps
import argparse
from xml.etree.ElementTree import fromstring
import glob
import concurrent.futures

parser = argparse.ArgumentParser(description='Convert XML to JSON')
parser.add_argument('-i', '--input_xml_folder', help='Path to the XML folder', default='./xml')
parser.add_argument('-o', '--output_json_folder', help='Path to the JSON folder', default='./json')
parser.add_argument('-max', '--max_threads', type=int, default=60)


def transform_xml_to_json(xml_file_input, json_file_output):
    """Transform Single File"""
    with open(xml_file_input, 'r') as f1:
        xml_text = f1.read()
    # Create directory to store output file , if already exists do nothing
    os.makedirs(os.path.dirname(json_file_output), exist_ok=True)
    with open(json_file_output, 'w') as f2:
        json_text = dumps(parker.data(fromstring((xml_text))))
        f2.write(json_text)


def worker(name):
    print('input file', name)
    # Change file name extension
    oname = os.path.splitext(name)[0] + '.json'
    # Create new file path
    ofile = os.path.join(args.output_json_folder, oname[len(args.input_xml_folder) + 1:])
    print('output file', ofile)
    transform_xml_to_json(name, ofile)


if __name__ == "__main__":
    args = parser.parse_args()
    print(args)

    with concurrent.futures.ProcessPoolExecutor(max_workers=args.max_threads) as executor:
        input_files = glob.iglob('{}/**/*.xml'.format(args.input_xml_folder), recursive=True)
        executor.map(worker, input_files)
    print('done')
