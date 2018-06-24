# Transforming XML to JSON
The aim of this program is to read XML files from an XML folder, and
transform them to JSON. This program is partially developed as `main.py` that performs
the transformation on a single file. 

The development task here is to enhance this program to work on multile folders using multiprocesses.
To be specific the requirements are: 

* **Requirement 1. Replicate folder structure:** This program should replicate the input_xml_folder structure to create
 the same structure for the JSON folder. Example of this is presented in <https://github.com/researchgraphsafe/f0023/tree/master/samples>
* **Requirement 2. Multiprocessing:** This program should process folders using separate threads up to the
MAX_THREADS identifier as in input parameter.That is running multiple copies of `process_folder`. 
This program is intended to run on a very large number of XML files (more than millions) that grouped in a nested 
folder structure. So the performance of this program is very important. 


Program `main.py` input arguments are:

* input_xml_folder: Path to the XML folder
* output_json_folder: Path to the JSON folder
* max_threads

and the output should be new JSON files in the output_json_folder that replicates the
structure of the XML folder. Example of this is presented `samples/original-xml` as input
and `samples/transformed-json`

 
**Note:** To complete this program please fork the repository, complete the code and
send a pull request. 
