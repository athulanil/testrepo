replace = 'a'
replace_with = 'z'

def replace_item(inst, parent_elem, index):
    flag = False
    if isinstance(inst, dict):
        for k, v in inst.items():
            if k == replace:
                inst[replace_with] = inst.pop(k)
                flag = True
            if flag:
                 replace_item(v, inst, replace_with)
            else:
                 replace_item(v, inst, k) 
    elif isinstance(inst, list):
        for n,i in enumerate(inst):
            replace_item(i, inst, n)

    else:
        if inst == replace:
            parent_elem[index] = replace_with

if __name__ == '__main__':
    di = {"a":"A","b":"B","c":[2,4,6,{"a":"A","b":"B"}],"d":{"a":[2,4,6],"b":[5,2,1]}}
    replace_item(di, 0, 0)
    print(di)