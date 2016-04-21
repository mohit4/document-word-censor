# document-word-censor
Python script search and replaces blacklisted words from a document using the list of words from json file.

## Using word_censor.py
#### Giving permission to python script
type and execute the following command

`$ chmod 777 word_censor.py`

#### General syntax
`$ word_censor.py <input_file> <output_file>`

output_file will contain censored text from input_file.
Note that output_file is optional. In case of only one command line argument i.e. the input_file, the censored text will be replace in the same file.
Eg. to censor contents of **Fifty_shades_of_Grey.txt**, the command will look like

`$ word_censor.py Fifty_shades_of_Grey.txt` 

## Improvements to be done
* Need to add command line options using python 'getopt' module
* Need to improve the **assistance** problem,
(the text 'assistance' becomes 'CENSOREDistance', if you know what I mean)
* Need to add a config file for debugging options
