mods_dic = {
    "CL": 0,
    "NO": 0,
    "NF": 1 << 0,
    "EZ": 1 << 1,
    "TD": 1 << 2,
    "HD": 1 << 3,
    "HR": 1 << 4,
    "SD": 1 << 5,
    "DT": 1 << 6,
    "RX": 1 << 7,
    "HT": 1 << 8,
    "NC": 1 << 9,
    "FL": 1 << 10,
    "AT": 1 << 11,
    "SO": 1 << 12,
    "RX2": 1 << 13,
    "PF": 1 << 14,
    "4K": 1 << 15,
    "5K": 1 << 16,
    "6K": 1 << 17,
    "7K": 1 << 18,
    "8K": 1 << 19,
    "FI": 1 << 20,
    "RD": 1 << 21,
    "Cinema": 1 << 22,
    "TG": 1 << 23,
    "9K": 1 << 24,
    "KC": 1 << 25,
    "1K": 1 << 26,
    "3K": 1 << 27,
    "2K": 1 << 28,
    "V2": 1 << 29,
    "MR": 1 << 30,
}


def calc_mods(mods: str) -> int:
    mods = mods2list(mods)
    num = 0
    for mod in mods:
        num ^= mods_dic.get(mod, 0)
    return num


def mods2list(args: str) -> list:
    args = args.replace(" ", "").replace(",", "").replace("，", "")
    args = args.upper()
    return [args[i : i + 2] for i in range(0, len(args), 2)]
