# Python API to Manipulate XBRL,iXBRL,OFX Formats

[Aspose.Finance for Python via .NET](https://products.aspose.com/finance/python-net) is a standalone on-premise API consisting of Python classes that allow you to process and manipuate finance-related formats, such as, XBRL, iXBRL and OFX.


## Finance File Processing via Python

- [Create XBRL instance](https://docs.aspose.com/finance/python-net/create-xbrl-files/) from scratch.
- Create iXBRL file from scratch.
- Create OFX request from scratch.
- Create OFX response from scratch.
- Read XBRL & iXBRL format.
- Read or write OFX request.
- Read or write OFX Response.
- Supports XBRL & iXBRL validation.
- Import and export XBRL & iXBRL format files.
- Handle the abstract element in XBRL taxonomy.
- Convert XBRL instance to iXBRL(inline XBRL).
- Convert iXBRL(inline XBRL) to XBRL.
- Convert XBRL instance to  to XLSX.
- Convert iXBRL(inline XBRL) to XLSX.
- Convert OFX request Version 1 to OFX request.
- Convert OFX response to OFX response Version 1.
- Validate XBRL instance.
- Validate iXBRL(inline XBRL)

## Read Finance Formats

XBRL, iXBRL, OFX

## System Requirements

### Supported Operating Systems

**Microsoft Windows&reg;:** Windows Desktop & Server (`x64`, `x86`)
**Linux:** Ubuntu, OpenSUSE, CentOS, and others
**Other:** Any operating system (OS) that can install Mono(.NET 4.0 Framework support) or use .NET core.

### Target Linux Platform

**Runtime Libraries:** `GCC-6` (or later)
**.NET Core:** Dependencies of .NET Core Runtime. Installing .NET Core Runtime itself is NOT required.
**For Python 3.5-3.7:** The `pymalloc` build of Python is needed. The `--with-pymalloc` Python build option is enabled by default. Typically, the `pymalloc` build of Python is marked with `m` suffix in the filename.
**Python Library:** `libpython` shared Python library

## Getting Started with Aspose.Finance for Python via .NET

### Installation via `pip`

The Aspose.Finance for Python via .NET is [available at pypi.org](https://pypi.org/project/aspose-finance/). To install it, please run the following command:

`pip install aspose-finance`

## Add Role Reference to XBRL Document

```python
xbrlDoc = XbrlDocument()
xbrlInstances = xbrlDoc.xbrl_instances
xbrlInstance = xbrlInstances[xbrlInstances.add()]
schemaRefs = xbrlInstance.schema_refs
schemaRefs.add(os.path.join(sourceDir, "schema.xsd"), "example", "http://example.com/xbrl/taxonomy")
schema = schemaRefs[0]
roleType = schema.get_role_type_by_uri("http://abc.com/role/link1")
if roleType is not None:
    roleReference = RoleReference(roleType)
    xbrlInstance.role_references.append(roleReference)
xbrlDoc.save(os.path.join(outputDir, "xbrl_sample_with_roletype.xbrl"))
```

[Home](https://www.aspose.com/) | [Product Page](https://products.aspose.com/finance/python-net) | [Docs](https://docs.aspose.com/finance/python-net/) | [Examples](https://github.com/aspose-finance/Aspose.finance-for-Python-via-.NET) | [Blog](https://blog.aspose.com/category/finance/) | [Search](https://search.aspose.com/) | [Free Support](https://forum.aspose.com/c/finance) | [Temporary License](https://purchase.aspose.com/temporary-license)
