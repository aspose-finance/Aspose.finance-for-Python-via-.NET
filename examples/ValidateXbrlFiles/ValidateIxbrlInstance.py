from aspose.finance.xbrl.inline import InlineXbrlDocument
from examples import Common

def Run():
    # The path to the documents directory.
    inputFile = Common.get_data_path("account_1.html")

    document = InlineXbrlDocument(inputFile)
    document.validate();
    if document.validation_errors.length > 0:
        validationErrors = document.validation_errors
