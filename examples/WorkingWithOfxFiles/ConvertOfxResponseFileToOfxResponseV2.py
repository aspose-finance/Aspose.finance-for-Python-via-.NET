from aspose.finance.ofx import OfxResponseDocument,OfxVersionEnum
from examples import Common

def Run():
    # The path to the documents directory.
    inputFile = Common.get_data_path("bankTransactionRes.sgml")
    outputFile = Common.get_output_path("bankTransactionRes.xml")

    # Convert OFX Response File from 1.03 to 2.2 format
    document = OfxResponseDocument(inputFile)
    document.save(outputFile, OfxVersionEnum.V2X)