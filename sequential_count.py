"""
Count the number of 'val's that exist in a field and number and format
them, incrementing the number each time one is found
"""
old = ""
cnt = 0
def seq_count(val):
    global old
    global cnt
    if old == val:
        cnt += 1
        ret = "{} {:04.0f}".format(val, cnt)
    else:
        cnt = 0
        ret = "{} {:04.0f}".format(val, cnt)
    old = val
    return ret
__esri_field_calculator_splitter__
seq_count(!Test!)