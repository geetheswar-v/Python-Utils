import requests

def converter(value, fro, to, unit):
    if unit == 'currency':
        url = f'https://v6.exchangerate-api.com/v6/e471daed4df82514a4370a89/latest/{fro.upper()}'
        response = requests.get(url)
        data = response.json()
        rate = data["conversion_rates"].get(to, 0)
        return round(value * float(rate), 2)
    from_this = get_units(unit)[fro][0]
    to_this = get_units(unit)[to][0]
    return round((value * to_this) / from_this, 6)


def get_units(unit):
    if unit == 'area':
        return AREA
    elif unit == 'digital_storage':
        return STORAGE
    elif unit == 'energy':
        return ENERGY
    elif unit == 'mass':
        return MASS
    elif unit == 'power':
        return POWER
    elif unit == 'temperature':
        return TEMPERATURE
    elif unit == 'volume':
        return VOLUME
    elif unit == 'currency':
        return CURRENCY
    return LENGTH


UNITS = ['length', 'area', 'digital_storage', 'energy', 'mass', 'power', 'temperature', 'volume', 'currency']


LENGTH = {
    'Meter': (1, 'm'),
    'Kilometer': (0.001, 'km'),
    'Miles': (0.0006, 'mi'),
    'Centimeter': (100, 'cm'),
    'Millimeter': (1000, 'mm'),
    'Micrometer': (1000000, 'um'),
    'Nanometer': (1000000000, 'nm'),
}

AREA = {
    'Meter': (1, 'm²'),
    'Kilometer': (0.000001, 'km²'),
    'Miles': (3.861e-7, 'mi²'),
    'Centimeter': (10000, 'cm²'),
    'Yard': (1.1959900463, 'yd'),
    'Foot': (1000000, 'ft'),
    'Inch': (1550.0031000062, 'in²'),
    'Acre': (0.0002471054, 'ac'),
}

STORAGE = {
    'kilobyte': (1, 'kb'),
    'Byte': (1024, 'B'),
    'Bit': (8192, 'b'),
    'Kilobit': (8, 'kb'),
    'Megabit': (0.0078125, 'Mb'),
    'Megabyte': (0.0009765625, 'MB'),
    'Gigabit': (0.0000076294, 'Gb'),
    'Gigabyte': (0.0000009537, 'GB'),
    'Terabit': (0.0000000075, 'Tb'),
    'Terabyte': (0.0000000009, 'TB'),
}

ENERGY = {
    'Joule': (1, 'J'),
    'Kilojoule': (0.001, 'kJ'),
    'Calorie': (0.2390057361, 'cal'),
    'Kilocalorie': (0.0002390057, 'kcal'),
    'Kilowatt-Hour': (0.0000002778, 'kW.h'),
}

MASS = {
    'Gram': (1, 'gm'),
    'Kilogram': (0.001, 'kg'),
    'Milligram': (1000, 'mg'),
    'Pound': (0.0022046226, 'lb'),
    'Ounce': (0.0352739619, 'OZ'),
    'Grain': (15.4323583529, 'gr'),
    'Stone': (0.000157473, 'st'),
    'Ton(metric)': (0.000001, 'T'),
    'Ton(US/short)': (0.0000011023, 'T'),
    'Ton(UK/long)': (0.0000009842, 'T'),
}

POWER = {
    'Watt': (1, 'W'),
    'Kilowatt': (0.001, 'kW'),
    'Megawatt': (0.000001, 'mW'),
    'HP(metric)': (0.0013596216, 'hp'),
    'HP(mechanical)': (0.0013410221, 'hp'),
    'ft-lbf/second': (0.7375621493, 'ft-lbf'),
    'Calorie/second': (0.2388458966, 'cal/s'),
    'BTU/second': (0.0009478171, 'btu/sec')
}

TEMPERATURE = {
    'Fahrenheit': (1, 'F'),
    'Kelvin': (255.9277777778, 'K'),
    'Celsius': (-17.2222222222, 'C'),
    'Rankine': (460, 'R'),
    'Delisle': (175.8333333333, 'D'),
    'Newton': (-5.6833333333, 'N'),
    'Reaumur': (-13.7777777778, 'Re'),
    'Romar': (-1.5416666667, 'R')
}

VOLUME = {
    'Liter': (1, 'L'),
    'Milliliter': (1000, 'ml'),
    'Teaspoon': (202.8841362111, 'tsp'),
    'Tablespoon': (67.6280454037, 'tbs'),
    'cup': (4.2267528377, 'C'),
    'Quart': (1.0566882094, 'qt'),
    'Gallon': (0.2641720524, 'gal'),
    'Barrel': (0.0083864144, 'bbl'),
    'Cubic cm': (1000, 'cm³'),
    'Cubic Meter': (0.001, 'm³'),
    'Cubic Inch': (61.0237440947, 'in³'),
    'Cubic Foot': (0.0353146667, 'ft³'),
    'Cubic Yard': (0.0013079506, 'y³'),
}

CURRENCY = {
    "INR": "₹",
    "USD": "$",
    "EUR": "€",
    "AED": "د.إ",
    "AFN": "؋",
    "ALL": "L",
    "AMD": "֏",
    "ANG": "ƒ",
    "AOA": "Kz",
    "ARS": "$",
    "AUD": "$",
    "AWG": "ƒ",
    "AZN": "₼",
    "BAM": "KM",
    "BBD": "$",
    "BDT": "৳",
    "BGN": "лв",
    "BHD": ".د.ب",
    "BIF": "FBu",
    "BMD": "$",
    "BND": "$",
    "BOB": "$b",
    "BRL": "R$",
    "BSD": "$",
    "BTN": "Nu.",
    "BWP": "P",
    "BYR": "Br",
    "BYN": "Br",
    "BZD": "BZ$",
    "CAD": "$",
    "CDF": "FC",
    "CHF": "CHF",
    "CLP": "$",
    "CNY": "¥",
    "COP": "$",
    "CRC": "₡",
    "CUC": "$",
    "CUP": "₱",
    "CVE": "$",
    "CZK": "Kč",
    "DJF": "Fdj",
    "DKK": "kr",
    "DOP": "RD$",
    "DZD": "دج",
    "EEK": "kr",
    "EGP": "£",
    "ERN": "Nfk",
    "ETB": "Br",
    "ETH": "Ξ",
    "FJD": "$",
    "FKP": "£",
    "GBP": "£",
    "GEL": "₾",
    "GGP": "£",
    "GHC": "₵",
    "GHS": "GH₵",
    "GIP": "£",
    "GMD": "D",
    "GNF": "FG",
    "GTQ": "Q",
    "GYD": "$",
    "HKD": "$",
    "HNL": "L",
    "HRK": "kn",
    "HTG": "G",
    "HUF": "Ft",
    "IDR": "Rp",
    "ILS": "₪",
    "IMP": "£",
    "IQD": "ع.د",
    "IRR": "﷼",
    "ISK": "kr",
    "JEP": "£",
    "JMD": "J$",
    "JOD": "JD",
    "JPY": "¥",
    "KES": "KSh",
    "KGS": "лв",
    "KHR": "៛",
    "KMF": "CF",
    "KPW": "₩",
    "KRW": "₩",
    "KWD": "KD",
    "KYD": "$",
    "KZT": "₸",
    "LAK": "₭",
    "LBP": "£",
    "LKR": "₨",
    "LRD": "$",
    "LSL": "M",
    "LTC": "Ł",
    "LTL": "Lt",
    "LVL": "Ls",
    "LYD": "LD",
    "MAD": "MAD",
    "MDL": "lei",
    "MGA": "Ar",
    "MKD": "ден",
    "MMK": "K",
    "MNT": "₮",
    "MOP": "MOP$",
    "MRO": "UM",
    "MRU": "UM",
    "MUR": "₨",
    "MVR": "Rf",
    "MWK": "MK",
    "MXN": "$",
    "MYR": "RM",
    "MZN": "MT",
    "NAD": "$",
    "NGN": "₦",
    "NIO": "C$",
    "NOK": "kr",
    "NPR": "₨",
    "NZD": "$",
    "OMR": "﷼",
    "PAB": "B/.",
    "PEN": "S/.",
    "PGK": "K",
    "PHP": "₱",
    "PKR": "₨",
    "PLN": "zł",
    "PYG": "Gs",
    "QAR": "﷼",
    "RMB": "￥",
    "RON": "lei",
    "RSD": "Дин.",
    "RUB": "₽",
    "RWF": "R₣",
    "SAR": "﷼",
    "SBD": "$",
    "SCR": "₨",
    "SDG": "ج.س.",
    "SEK": "kr",
    "SGD": "$",
    "SHP": "£",
    "SLL": "Le",
    "SOS": "S",
    "SRD": "$",
    "SSP": "£",
    "STD": "Db",
    "STN": "Db",
    "SVC": "$",
    "SYP": "£",
    "SZL": "E",
    "THB": "฿",
    "TJS": "SM",
    "TMT": "T",
    "TND": "د.ت",
    "TOP": "T$",
    "TRL": "₤",
    "TRY": "₺",
    "TTD": "TT$",
    "TVD": "$",
    "TWD": "NT$",
    "TZS": "TSh",
    "UAH": "₴",
    "UGX": "USh",
    "UYU": "$U",
    "UZS": "лв",
    "VEF": "Bs",
    "VND": "₫",
    "VUV": "VT",
    "WST": "WS$",
    "XAF": "FCFA",
    "XBT": "Ƀ",
    "XCD": "$",
    "XOF": "CFA",
    "XPF": "₣",
    "YER": "﷼",
    "ZAR": "R",
    "ZWD": "Z$",
}


if __name__ == '__main__':
    print(converter(1, 'USD', 'INR', 'currency'))
