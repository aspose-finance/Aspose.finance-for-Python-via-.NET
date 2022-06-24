#!/usr/bin/env python3
from examples.Conversion import ConvertXbrlToIXbrl,ConvertXbrlToXlsx
from examples.CreateXbrlFiles import AddArcRoleReferenceToXbrlDocument,AddContextToXbrlDocument,AddFootnoteLinkToXbrlDocument,AddItemToXbrlDocument,AddRoleReferenceToXbrlDocument,AddSchemaReferenceToXbrlDocument,AddUnitToXbrlDocument,CreateXbrlFile
from examples.ReadXbrlFiles import ReadIxbrlDocument,ReadXbrlDocument
from examples.ValidateXbrlFiles import ValidateIxbrlInstance,ValidateXbrlInstance,ValidateXBRLWithStardardErrorMessage
from examples.WorkingWithOfxFiles import ConvertOfxRequestFileToOfxRequestV2,ConvertOfxResponseFileToOfxResponseV2,CreateOfxBankTransactionRequestFile,CreateOfxBankTransactionResponseFile



print("Open RunExamples.py. \nIn Main() method uncomment the example that you want to run.")
print("=====================================================")


# Uncomment the one you want to try out          

# =====================================================
# =====================================================
# Conversion
# =====================================================
# =====================================================

ConvertXbrlToIXbrl.Run()
ConvertXbrlToXlsx.Run() 

# =====================================================
# =====================================================
# CreateXbrlFiles
# =====================================================
# =====================================================

AddArcRoleReferenceToXbrlDocument.Run()
AddContextToXbrlDocument.Run()
AddFootnoteLinkToXbrlDocument.Run()
AddItemToXbrlDocument.Run() 
AddRoleReferenceToXbrlDocument.Run() 
AddSchemaReferenceToXbrlDocument.Run()
AddUnitToXbrlDocument.Run()
CreateXbrlFile.Run()

# =====================================================
# =====================================================
# ReadXbrlFiles
# =====================================================
# =====================================================

ReadIxbrlDocument.Run()
ReadXbrlDocument.Run()

# =====================================================
# =====================================================
# ValidateXbrlFiles
# =====================================================
# =====================================================

ValidateIxbrlInstance.Run()
ValidateXbrlInstance.Run()
ValidateXBRLWithStardardErrorMessage.Run()

# =====================================================
# =====================================================
# Asset WorkingWithOfxFiles
# =====================================================
# =====================================================
ConvertOfxRequestFileToOfxRequestV2.Run()
ConvertOfxResponseFileToOfxResponseV2.Run()
CreateOfxBankTransactionRequestFile.Run()
CreateOfxBankTransactionResponseFile.Run()

# Stop before exiting
print("\n\nProgram Finished.")
