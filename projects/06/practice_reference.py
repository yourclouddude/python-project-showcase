from decimal import Decimal
def money(text):
    value=Decimal(str(text))
    if not value.is_finite() or value<0 or value.as_tuple().exponent < -2:
        raise ValueError('Use nonnegative two-place money.')
    return value.quantize(Decimal('0.01'))
