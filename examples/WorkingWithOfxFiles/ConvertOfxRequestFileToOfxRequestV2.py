from aspose.finance.ofx import OfxRequestDocument,OfxVersionEnum
from examples import Common

def Run():
    # The path to the documents directory.
    inputFile = Common.get_data_path("bankTransactionReq.sgml")
    outputFile = Common.get_output_path("bankTransactionReq.xml")
    # Convert OFX Request File from 1.03 to 2.2 format
    document = OfxRequestDocument(inputFile)
    document.save(outputFile, OfxVersionEnum.V2X)
