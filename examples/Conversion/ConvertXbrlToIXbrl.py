﻿from aspose.finance.xbrl import XbrlDocument,SaveOptions,SaveFormat
from examples import Common

def Run():
    # The path to the documents directory.
    inputFile = Common.get_data_path("IdScopeContextPeriodStartAfterEnd.xml")
    outputFile = Common.get_output_path("Converted-Xbrl-To-IXBRL_out.html")

    document = XbrlDocument(inputFile)

    # Set save options
    Opts = SaveOptions()
    Opts.save_format = SaveFormat.IXBRL

    # Save file to iXBRL format
    document.save(outputFile, Opts)
