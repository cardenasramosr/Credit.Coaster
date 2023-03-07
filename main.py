from schemas.user import User 
from schemas.transaction import Transaction
from schemas.payment import Payment
from schemas.card import Card
from schemas.account import Account

from controllers.user_controller import UserController  as UC
from controllers.transaction_controller import TransactionController as TC
from controllers.payment_controller import PaymentController as PC
from controllers.card_controller import CardController as CC
from controllers.account_controller import AccountController as AC 


name = "Ricardo Cardenas"
birthdate = "12-12-98"
phone = "123456789"

User1 = UC.create_user(name,birthdate,phone)
Acc = AC.create_account(User1,10000)
Card = CC.create_card(Acc,1234)
payment = PC.create_payment(Card,100)
transaction = TC.create_transaction(Card,200,1234)


print(f"Nombre",User1.name)
print(f"Transaccion:-",(transaction.amount))
print(f"Abono:",payment.amount)
print(f"Balance:",Card.account.balance)

no_pasa = TC.create_transaction(Card,200,1234)
print(f"Transaccion:",no_pasa.amount)




