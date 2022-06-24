from aspose.finance.xbrl import XbrlDocument
from examples import Common

def Run():
    # The path to the documents directory.
    inputFile = Common.get_data_path("IdScopeContextPeriodStartAfterEnd.xml")

    document = XbrlDocument(inputFile)

    xbrlInstances = document.xbrl_instances
    xbrlInstance = xbrlInstances[0]
    facts = xbrlInstance.facts
    schemaRefs = xbrlInstance.schema_refs
    contexts = xbrlInstance.contexts
    units = xbrlInstance.units
