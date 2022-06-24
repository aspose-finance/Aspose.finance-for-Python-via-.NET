from aspose.finance.xbrl import XbrlDocument,ArcroleReference
from examples import Common

def Run():
    # The path to the documents directory.
    outputFile = Common.get_output_path("document8.xbrl")
    inputSchemaFile = Common.get_data_path("schema.xsd")

    xbrlDoc = XbrlDocument()
    xbrlInstances = xbrlDoc.xbrl_instances
    xbrlInstance = xbrlInstances[xbrlInstances.add()]
    schemaRefs = xbrlInstance.schema_refs
    schemaRefs.add(inputSchemaFile, "example", "http://example.com/xbrl/taxonomy")
    schema = schemaRefs[0]
    arcroleType = schema.get_arcrole_type_by_uri("http://abc.com/arcrole/footnote-test")
    if arcroleType is not None:
        arcroleReference = ArcroleReference(arcroleType)
        xbrlInstance.arcrole_references.append(arcroleReference)
    xbrlDoc.save(outputFile)
