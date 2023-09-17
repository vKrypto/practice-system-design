from datetime import datetime
from .utils import process_pdf_file, get_bills_from_email

class EmailAuthenticationError(Exception):
    pass


class CardType:
    type: str = None
    bank: str = None



class EmailAuthorization:

    email_auth_token: str = None
    last_checked_date: datetime = None

    def get_bills(self):
        # try fecthing bills from email access token
        bills = get_bills_from_email(self.email_auth_token, from_date=self.last_checked_date, subject_string="statement")
    
        self.last_checked_date = datetime.now()
        self.save()

        return bills



class Card:
    account_id: str = None
    card_number: str = None

    card_type: CardType = None
    email_autorization: EmailAuthorization = None

    card_active_date: datetime = None 
    billing_date: datetime = None # next billing date

    last_bill_amount:int = None
    cur_out_standing_amount:int = None


    def all_bills(self):
        pass

    def all_payments(self):
        pass

    def is_email_authorized(self):
        return self.email_autorization != None
    
    def authorize_email_for_bill(self):
        pass

    def check_for_bills(self):
        # run this after billing_date
        if self.email_autorization:
            try:
                bills = self.email_autorization.get_bills()
                for bill in bills:
                    self._add_new_bill(bill)
            except EmailAuthenticationError:
                self.email_autorization = None
                self.save()



    def _add_new_bill(self, pdf_file):
        data = process_pdf_file(pdf_file)

        # step 1: add bill
        bill = self.bills.create(bill_amount=data['bill_amount'], bill_date=data['billing_date'], bill_pdf_file_url=pdf_file)
        # step 2: add bill transactions
        for txn in data['transactions']:
            bill.add_transaction(**txn)

        # update cur objects
        self.cur_out_standing_amount -= data['bill_amount']
        self.last_bill_amount = data['bill_amount']
        self.save()


    def add_payment(self, amount, transaction_id):
        # authenticated from our side, initialized payment
        payment_obj = self.paments.create(amount=amount, txn_id=transaction_id)
        billPaymentSettlementObserver(card, payment_obj)


class CardBill:
    card: Card = None
    
    bill_date: datetime = None
    bill_amount: int =  None
    bill_pdf_file_url:str = None


    def hidden_charges(self):
        pass

    def category_wise_aggregate(self):
        pass


class BillTransaction:
    card_bill: CardBill = None  # relationship is transactions

    txn_amount: int = None
    category: str = None


class BillPayment:
    # all payments must be authorized and successful
    card: Card = None # relationship is payments

    amount: int = None
    txn_id: int = None
    created_date: int = None
    settled_date: int = None

    # observer pattern
    @notify_user(content="BIll payment was settled.")
    def mark_as_settled(self):
        if not self.settled_date:
            self.settled_date = datetime.now()

class billPaymentSettlementObserver:
    bill_payment: BillPayment = None # relationship is payments
    card: Card = None
    is_settled: bool = False
    
    def check_update(self):
        if not self.is_settled:
            self.is_settled = self.card.enquire_bank_for_txn(txn_id=self.bill_payment.txn_id)
            if self.is_settled:
                self.bill_payment.mark_as_settled()
            self.save()