import re

def format_phone(value):
    if value is None:
        return None

    phone = re.sub('[^0-9\+]', '', value)

    if len(phone) > 7:
        phone = re.sub('^\+7', '', phone)
        phone = re.sub('^79|89', '9', phone)
        phone = re.sub('^78|88', '8', phone)

    return phone