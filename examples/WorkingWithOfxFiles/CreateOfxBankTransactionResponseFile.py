from aspose.finance.ofx import OfxResponseDocument,SignonResponseMessageSetV1,BankResponseMessageSetV1,BankAccount,Status,OfxVersionEnum,SeverityEnum,CurrencyEnum,AccountEnum,BankTransactionList,StatementTransaction,TransactionEnum,LedgerBalance,AvailableBalance
from aspose.finance.ofx.signon import SignonResponse,FinancialInstitution
from aspose.finance.ofx.bank import StatementTransactionResponse,StatementResponse
from examples import Common
def Run():
    # The path to the documents directory.
    outputFile = Common.get_output_path("newOfxResponseBankStatement.xml")
    outputFile1 = Common.get_output_path("newOfxResponseBankStatement.sgml")
    ofxResponseDoc = OfxResponseDocument()
    ofxResponseDoc.signon_response_message_set_v1 = SignonResponseMessageSetV1()
    signonResponse = SignonResponse()
    ofxResponseDoc.signon_response_message_set_v1.signon_response = signonResponse
    signonResponse.status = Status()
    signonResponse.status.code = "0"
    signonResponse.status.severity = SeverityEnum.INFO
    signonResponse.status.message = "SUCCESS"
    signonResponse.server_date = "20200611"
    signonResponse.profile_update_date = "20200611"
    fi = FinancialInstitution()
    fi.organization = "aspose"
    fi.financial_institution_id = "1"
    signonResponse.financial_institution = fi
    signonResponse.session_cookie = "11111111111111111"

    ofxResponseDoc.bank_response_message_set_v1 = BankResponseMessageSetV1()
    stmtTransResponse = StatementTransactionResponse()
    ofxResponseDoc.bank_response_message_set_v1.statement_transaction_responses.append(stmtTransResponse)
    stmtTransResponse.transaction_unique_id = "829631324"
    stmtTransResponse.status = Status()
    stmtTransResponse.status.code = "0"
    stmtTransResponse.status.severity = SeverityEnum.INFO
    stmtTransResponse.statement_response = StatementResponse()
    stmtTransResponse.statement_response.currency = CurrencyEnum.USD
    stmtTransResponse.statement_response.bank_account_from = BankAccount()
    stmtTransResponse.statement_response.bank_account_from.bank_id = "1111111"
    stmtTransResponse.statement_response.bank_account_from.account_id = "1111111111111"
    stmtTransResponse.statement_response.bank_account_from.account_type = AccountEnum.CHECKING
    stmtTransResponse.statement_response.bank_transaction_list = BankTransactionList()
    stmtTransResponse.statement_response.bank_transaction_list.start_date = "20200601000000"
    stmtTransResponse.statement_response.bank_transaction_list.end_date = "20200611000000"
    transaction1 = StatementTransaction()
    transaction1.transaction_type = TransactionEnum.DEBIT
    transaction1.posted_date = "20200611000000"
    transaction1.transaction_amount = "-12"
    transaction1.financial_institution_transaction_id = "1111111111111111111111111"
    transaction1.name = "bbbbbbbbbbbbbbbbbbbbbbb"
    transaction2 = StatementTransaction()
    transaction2.transaction_type = TransactionEnum.CREDIT
    transaction2.posted_date = "20200611000000"
    transaction2.transaction_amount = "22222.11"
    transaction2.financial_institution_transaction_id = "2222222222222222222222222222"
    transaction2.name = "wwwwwwwwwwwwwwwwwwwwwwww"
    stmtTransResponse.statement_response.bank_transaction_list.statement_transactions.append(transaction1)
    stmtTransResponse.statement_response.bank_transaction_list.statement_transactions.append(transaction2)
    stmtTransResponse.statement_response.ledger_balance = LedgerBalance()
    stmtTransResponse.statement_response.ledger_balance.balance_amount = "+2222.42"
    stmtTransResponse.statement_response.ledger_balance.date_as_of = "20200611000000"
    stmtTransResponse.statement_response.available_balance = AvailableBalance()
    stmtTransResponse.statement_response.available_balance.balance_amount = "+222222.42"
    stmtTransResponse.statement_response.available_balance.date_as_of = "20200611000000"

    ofxResponseDoc.save(outputFile, OfxVersionEnum.V2X)
    ofxResponseDoc.save(outputFile1, OfxVersionEnum.V1X)
