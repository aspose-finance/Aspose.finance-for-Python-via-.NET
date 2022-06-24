import datetime
from aspose.finance.xbrl import XbrlDocument,Unit,QualifiedName,UnitType
from examples import Common

def Run():
    # The path to the documents directory.
    outputFile = Common.get_output_path("document4.xbrl")

    xbrlDoc = XbrlDocument()
    xbrlInstances = xbrlDoc.xbrl_instances
    xbrlInstance = xbrlInstances[xbrlInstances.add()]
    unit = Unit(UnitType.MEASURE)
    unit.measure_qualified_names.append(QualifiedName("USD", "iso4217", "http://www.xbrl.org/2003/iso4217"))
    xbrlInstance.units.append(unit)
    xbrlDoc.save(outputFile)

