from datetime import datetime
from aspose.finance.xbrl import XbrlDocument,ContextPeriod,ContextEntity,Context
from examples import Common

def Run():
    # The path to the documents directory.
    outputFile = Common.get_output_path("document3.xbrl")

    xbrlDoc = XbrlDocument()
    xbrlInstances = xbrlDoc.xbrl_instances
    xbrlInstance = xbrlInstances[xbrlInstances.add()]
    contextPeriod = ContextPeriod(datetime(2020,1,1), datetime(2020,2,10))
    contextEntity = ContextEntity("exampleIdentifierScheme", "exampleIdentifier")
    context = Context(contextPeriod, contextEntity)
    xbrlInstance.contexts.append(context)
    xbrlDoc.save(outputFile)