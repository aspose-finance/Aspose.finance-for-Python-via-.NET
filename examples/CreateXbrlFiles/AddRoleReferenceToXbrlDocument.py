from aspose.finance.xbrl import XbrlDocument,RoleReference
from examples import Common

def Run():
    # The path to the documents directory.
    outputFile = Common.get_output_path("document7.xbrl")
    inputSchemaFile = Common.get_data_path("schema.xsd")

    xbrlDoc = XbrlDocument()
    xbrlInstances = xbrlDoc.xbrl_instances
    xbrlInstance = xbrlInstances[xbrlInstances.add()]
    schemaRefs = xbrlInstance.schema_refs
    schemaRefs.add(inputSchemaFile, "example", "http://example.com/xbrl/taxonomy")
    schema = schemaRefs[0]
    roleType = schema.get_role_type_by_uri("http://abc.com/role/link1")
    if roleType is not None:
        roleReference = RoleReference(roleType)
        xbrlInstance.role_references.append(roleReference)
    xbrlDoc.save(outputFile)
