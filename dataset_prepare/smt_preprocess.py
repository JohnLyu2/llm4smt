def _get_text(path):
    with open(path, "r") as f:
        text = f.read()
    return text

# items mean contents within a top-level parenthesis
def _get_items(text):
    items = []
    item = ""
    count = 0
    for c in text:
        if c == "(":
            count += 1
        elif c == ")":
            count -= 1
        item += c
        if count == 0:
            if item.startswith("("):
                items.append(item)
            item = ""
    return items

# return a text with just one line of all assertions
def get_assertions(path):
    text = _get_text(path)
    items = _get_items(text)
    assertion_lst = []
    for item in items:
        if item.startswith("(assert"):
            assertion_lst.append(item)
    assertions = ""
    for assertion in assertion_lst:
        assertions += assertion.replace("\n", " ")
    return assertions
    

# assertions = get_assertions("/Users/zhengyanglumacmini/Desktop/Projects/MachSMT/benchmarks/smt-lib/non-incremental/BV/2017-Preiner-keymaera/accelerating-node2100.smt2")
# print(f"assertions: {assertions}")

# assertions2 = get_assertions("smt_files/testing/bv0_smt2.smt2")
# print(f"assertions2: {assertions2}")
