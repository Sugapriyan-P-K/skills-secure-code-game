'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

max_item_amount = 100000
max_quantity = 100
max_total = 1e6

def validorder(order: Order):
    net = 0
    
    for item in order.items:
        if item.type == 'payment':
            if item.amount > -1 * max_item_amount and item.amount < max_item_amount:
                net += int(item.amount)
        elif item.type == 'product':
            if item.quantity > 0 and item.quantity <= max_quantity and item.amount > 0 and item.amount <= max_item_amount:
                net -= int(item.amount) * item.quantity
            if net > max_total or net < -1 * max_total:
                return ("max amount exceeded")
        else:
            return("Invalid item type: %s" % item.type)
    
    if int(net) != 0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
