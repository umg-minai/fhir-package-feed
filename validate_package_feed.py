import lxml.etree as ET

schema_doc = ET.parse('schema/package-feed-schema.xsd')
schema = ET.XMLSchema(schema_doc)

xml_doc = ET.parse('package-feed.xml')

if not schema.validate(xml_doc):
    for error in schema.error_log:
        print(f"Error ({error.filename}:{error.line}): {error.message}")
    raise Exception("XML validation failed")
else:
    print("XML is valid")
