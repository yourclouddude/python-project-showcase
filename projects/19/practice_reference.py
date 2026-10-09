from decimal import Decimal,InvalidOperation
def invoice_total(quantity, rate):
    try:
        value=Decimal(str(rate))
    except InvalidOperation as error:
        raise ValueError('Invalid rate.') from error
    if type(quantity) is not int or not 1<=quantity<=10000 or not value.is_finite() or not 0<=value<=1000000 or value.as_tuple().exponent < -2:
        raise ValueError('Invalid quantity/rate.')
    return format(value*quantity,'.2f')
