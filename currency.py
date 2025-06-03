
def round_rate(rate):
    
    return round(rate, 4)


def reverse_rate(rate):
    
    if rate != 0:
        return round(1 / rate, 4)
    return 0

def format_output(date, from_currency, to_currency, rate, amount):
    
    converted_amount = round(rate * amount, 2)
    inverse = reverse_rate(rate)
    return (
        f"The conversion rate on {date} from {from_currency} to {to_currency} was {rate}. "
        f"So {amount} in {from_currency} correspond to {converted_amount} in {to_currency}. "
        f"The inverse rate was {inverse}."
    )
    