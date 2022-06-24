from aspose.finance.xbrl import XbrlDocument,RoleReference
from examples import Common

def Run():
    # The path to the documents directory.
    outputFile = Common.get_output_path("document2.xbrl")
    inputSchemaFile = Common.get_data_path("schema.xsd")

    xbrlDoc = XbrlDocument()
    xbrlInstances = xbrlDoc.xbrl_instances
    xbrlInstance = xbrlInstances[xbrlInstances.add()]
    schemaRefs = xbrlInstance.schema_refs
    schemaRefs.add(inputSchemaFile, "example", "http://example.com/xbrl/taxonomy")
    xbrlDoc.save(outputFile)
