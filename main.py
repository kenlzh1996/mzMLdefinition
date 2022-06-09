import re
import numpy as np
import pandas as pd

# this code is to generate mzMLdef.txt, a txt file that contains 5 columns with no header
# the 5 columns are: file path, instrument name, set number, fraction method, fraction number

#### first column: file path
# file_name.txt is a txt file with all the mzML file names (copy all file name to the file_name.txt first)
# this code applies for mzML file name that looks like this EAPSDL_1_30_TMT16_Set02_IPG3to10_800ug_20210808_fr04.mzML
filename = pd.read_csv("file_name.txt", header=None, sep='\t')
filename = filename[0].to_list()
## concatenate the file path to file name
filepath = "/home/ec2-user/mzML_files/"

complete_file_name = []
for i in filename:
    complete_file_name.append(filepath+i)

#### second column: instrument name
instrument_name = np.repeat('qehf', len(complete_file_name))

#### third column: extract set number from file name
set_number=[]
for i in complete_file_name:
    s = i.split("_")
    set_number.append(s[5])

#### fourth column: fraction method
fraction_method = np.repeat('ph310', len(complete_file_name))

#### fifth column: fraction number
fraction_number=[]
for i in complete_file_name:
    s = re.findall('[0-9]+', i)
    if len(s[-1]) > 2:
        fraction_number.append(s[-2])
    else:
        fraction_number.append(s[-1])

#### final file assembly:
mzMLdef = pd.DataFrame([complete_file_name, instrument_name, set_number, fraction_method, fraction_number]).transpose()
mzMLdef.to_csv("mzMLdef.txt", header=None, index=None, sep='\t')