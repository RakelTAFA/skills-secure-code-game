'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

'''
Bug test_6 : le calcul de nombre énorme pose un problème de précision, ajouter et soustraire 1e19 fait 0.0
             mais faire "-1000 + 1e19 - 1e19" donne aussi 0.0 car le petit nombre est absorbée par la précision des nombres énormes
Solution   : utiliser le module decimal et le type Decimal

Bug test_7 : les calculs sur les nombres ne donnent pas exactement les bons résultats, 1.1 + 2.2 = 3.300...03 != 3.3
             Donc le programme considère que la somme n'a pas été payé et qu'il reste une balance de 0.00$ (à cause de l'imprécision)
             --> Même problème en utilisant le module Decimal
Solution   : Utiliser la méthode round intégrée à Python pour enlever ces imprécisions.


'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = 0

    for item in order.items:
        if item.type == 'payment':
            net += Decimal(item.amount)
        elif item.type == 'product':
            net -= Decimal(item.amount * item.quantity)
        else:
            return "Invalid item type: %s" % item.type
        net = round(net, 2)

    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id