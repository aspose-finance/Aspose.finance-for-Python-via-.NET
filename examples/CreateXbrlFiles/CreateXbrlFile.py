from aspose.finance.xbrl import XbrlDocument
from examples import Common

def Run():
    # The path to the documents directory.
    outputFile = Common.get_output_path("document1.xbrl")

    xbrlDoc = XbrlDocument()
    xbrlInstances = xbrlDoc.xbrl_instances
    xbrlInstance = xbrlInstances[xbrlInstances.add()]
    xbrlDoc.save(outputFile)
