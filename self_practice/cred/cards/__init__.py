from .models import Card


all_cards = Card.objects.filter(account_id = 3123123123)
for card in all_cards:
    print({
        "card_number": card.card_number,
        "card_type": card.card_type,
        "card_name": card.card_name,
    })


card = all_cards.filter(card_number=1231_2312_1231_1212)



all_bills = card.bills.all()
