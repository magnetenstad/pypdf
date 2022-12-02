from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from pathlib import Path
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def extract(name, ranges):
	pdf_reader = PdfFileReader(f"input/{name}.pdf")
	pdf_writer = PdfFileWriter()
	for r in ranges:
		for n in range(r[0]-1, r[1]):
			page = pdf_reader.getPage(n)
			pdf_writer.addPage(page)

	with Path(f"output/{name}{ranges}.pdf").open(mode="wb") as output_file:
		pdf_writer.write(output_file)

def merge_folder(folder):
	inputfolder = f"input/{folder}"
	pdf_merger = PdfFileMerger(strict = False)
	for filename in os.listdir(inputfolder):
		pdf = PdfFileReader(f"{inputfolder}/{filename}")
		pdf_merger.append(pdf)
		
	with Path(f"output/{folder}.pdf").open(mode="wb") as output_file:
		pdf_merger.write(output_file)
