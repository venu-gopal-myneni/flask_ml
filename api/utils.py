
def process_list(alist):
    data = ""
    for te in alist:
        data = f"{data},{str(te)}"
    if len(data)>0:
        data = data[1:]
    return data