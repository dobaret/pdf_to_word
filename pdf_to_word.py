from pdf2docx import Converter
import os
import datetime
import pytz

# source file as environment variable
pdf_file = 'source/' + os.environ['PDF_FILE']

if not pdf_file.endswith('.pdf'):
    pdf_file += '.pdf'

# get the base name of the pdf file
base_name = os.path.splitext(os.path.basename(pdf_file))[0]  

# set the desired time zone
time_zone = pytz.timezone("Europe/Paris")  

# add time stamp to the output file name
current_date_time = datetime.datetime.now(time_zone).strftime("%d-%m-%Y_%H-%M")

# the output folder
output_folder = 'output' 

# destination file in the output folder with date and time added
docx_file = os.path.join(output_folder, base_name + '_' + current_date_time + '.docx')

# create the output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()
