from datetime import datetime
from aspose.finance.xbrl import XbrlDocument,ContextPeriod,ContextEntity,Context,FootnoteLink,Footnote,Loc,FootnoteArc
from examples import Common

def Run():
    # The path to the documents directory.
    outputFile = Common.get_output_path("document6.xbrl")
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
    footnoteLink = FootnoteLink()
    footnote = Footnote("footnote1")
    footnote.text = "Including the effects of the merger."
    loc = Loc("#cd1", "fact1")
    footnoteArc = FootnoteArc(loc.label, footnote.label)
    footnoteLink.footnotes.append(footnote)
    footnoteLink.locators.append(loc)
    footnoteLink.footnote_arcs.append(footnoteArc)
    xbrlInstance.footnote_links.append(footnoteLink)
    xbrlDoc.save(outputFile)