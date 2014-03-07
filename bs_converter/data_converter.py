__author__ = 'archmagece'


def to_number(num_str):
    if len(str().strip()) == 0:
        return 0
    else:
        try:
            return int(num_str)
        except:
            try:
                return float(num_str)
            except:
                return None
    pass
