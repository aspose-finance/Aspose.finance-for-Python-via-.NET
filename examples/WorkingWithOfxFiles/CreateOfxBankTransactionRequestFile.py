from aspose.finance.ofx import OfxRequestDocument,SignonRequestMessageSetV1,BankRequestMessageSetV1,BankAccount,IncTransaction,OfxVersionEnum,AccountEnum
from aspose.finance.ofx.signon import SignonRequest,FinancialInstitution
from aspose.finance.ofx.bank import StatementTransactionRequest,StatementRequest
from examples import Common

def Run():
    # The path to the documents directory.
    outputFile = Common.get_output_path("newOfxRequestBankStatement.xml")
    outputFile1 = Common.get_output_path("newOfxRequestBankStatement.sgml")

    ofxRequestDoc = OfxRequestDocument()
    ofxRequestDoc.signon_request_message_set_v1 = SignonRequestMessageSetV1()
    signonRequest = SignonRequest()
    ofxRequestDoc.signon_request_message_set_v1.signon_request = signonRequest
    signonRequest.client_date = "20200611000000"
    signonRequest.user_id = "aspose"
    signonRequest.user_password = "password"
    fi = FinancialInstitution()
    fi.organization = "aspose"
    fi.financial_institution_id = "1"
    signonRequest.financial_institution = fi
    signonRequest.app_version = "1.0"
    signonRequest.app_id = "Aspose.Finance"
    signonRequest.client_user_id = "aaaaaaa"

    ofxRequestDoc.bank_request_message_set_v1 = BankRequestMessageSetV1()
    stmtTransRequest = StatementTransactionRequest()
    ofxRequestDoc.bank_request_message_set_v1.statement_transaction_requests.append(stmtTransRequest)
    stmtTransRequest.transaction_unique_id = "1111111"
    stmtTransRequest.statement_request = StatementRequest()
    stmtTransRequest.statement_request.bank_account_from = BankAccount()
    stmtTransRequest.statement_request.bank_account_from.bank_id = "sssss"
    stmtTransRequest.statement_request.bank_account_from.account_id = "sfsdfsfsdf"
    stmtTransRequest.statement_request.bank_account_from.account_type = AccountEnum.CHECKING
    stmtTransRequest.statement_request.inc_transaction = IncTransaction()
    stmtTransRequest.statement_request.inc_transaction.start_date = "20200601000000"
    stmtTransRequest.statement_request.inc_transaction.end_date = "20200611000000"
    stmtTransRequest.statement_request.inc_transaction.include = True

    ofxRequestDoc.save(outputFile, OfxVersionEnum.V2X)
    ofxRequestDoc.save(outputFile1, OfxVersionEnum.V1X)

