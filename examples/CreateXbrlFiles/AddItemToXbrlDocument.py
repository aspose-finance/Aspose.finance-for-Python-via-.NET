from datetime import datetime
from aspose.finance.xbrl import XbrlDocument,ContextPeriod,ContextEntity,Context,Unit,UnitType,QualifiedName,Item
from examples import Common

def Run():
    # The path to the documents directory.
    outputFile = Common.get_output_path("document5.xbrl")
    inputSchemaFile = Common.get_data_path("schema.xsd")

    xbrlDoc = XbrlDocument()
    xbrlInstances = xbrlDoc.xbrl_instances
    xbrlInstance = xbrlInstances[xbrlInstances.add()]
    schemaRefs = xbrlInstance.schema_refs
    schemaRefs.add(inputSchemaFile, "example", "http://example.com/xbrl/taxonomy")
    schema = schemaRefs[0]
    contextPeriod = ContextPeriod(datetime(2020,1,1), datetime(2020,2,10))
    contextEntity = ContextEntity("exampleIdentifierScheme", "exampleIdentifier")
    context = Context(contextPeriod, contextEntity)
    xbrlInstance.contexts.append(context)
    unit = Unit(UnitType.MEASURE)
    unit.measure_qualified_names.append(QualifiedName("USD", "iso4217", "http://www.xbrl.org/2003/iso4217"))
    xbrlInstance.units.append(unit)
    fixedAssetsConcept = schema.get_concept_by_name("fixedAssets")
    if fixedAssetsConcept is not None:
        item = Item(fixedAssetsConcept)
        item.context_ref = context
        item.unit_ref = unit
        item.precision = 4
        item.value = "1444"
        xbrlInstance.facts.append(item)
    xbrlDoc.save(outputFile)
