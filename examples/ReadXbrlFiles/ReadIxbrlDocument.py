from aspose.finance.xbrl.inline import InlineXbrlDocument
from examples import Common

def Run():
    # The path to the documents directory.
    inputFile = Common.get_data_path("account_1.html")

    document = InlineXbrlDocument(inputFile)

    inlineFacts = document.facts
    contexts = document.contexts
    units = document.units