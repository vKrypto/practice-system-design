
def process_pdf_file(pdf_file_url):
    """
    do some OCR stuff and process the pdf file from url fetch.
    Args:
        pdf_file_url (str): URL OF the pdf file
    Returns:
        dict: bill summary along with all the transactions
    """
    return {

    }


def get_bills_from_email(self, email_auth_token, from_date, subject_str):
    """scan the email for statements after from_date till now.

    Args:
        email_auth_token (str): _description_
        from_date (datetime, optional): _description_
        subject_str (_type_): _description_

    Returns:
        list: list of email_bills
    """
    return []