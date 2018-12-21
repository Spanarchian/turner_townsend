from fifthstack import executer as ex


def test_empty_stack():
    act = ex(["CLEAR"])
    assert act == []


def test_swap_no_elem():
    ex(["CLEAR"])
    act = ex(["SWAP"])
    assert act == "ERROR"


def test_swap_one_elem():
    ex(["CLEAR"])
    ex(["PUSH",10])
    act = ex(["SWAP"])
    assert act == "ERROR"


def test_swap_two_elem():
    ex(["CLEAR"])
    ex(["PUSH", 10])
    ex(["PUSH", 100])
    act = ex(["SWAP"])
    assert act == [100, 10]


def test_swap_two_action_elem():
    ex(["CLEAR"])
    ex(["PUSH", 10])
    ex(["PUSH", 100])
    ex(["/"])
    act = ex(["SWAP"])
    assert act == "ERROR"


def test_div_two_elem():
    ex(["CLEAR"])
    ex(["PUSH", 10])
    ex(["PUSH", 100])
    act = ex(["/"])
    assert act == [10]


def test_div_two_elem_less_than_1():
    ex(["CLEAR"])
    ex(["PUSH", 100])
    ex(["PUSH", 10])
    act = ex(["/"])
    assert act == "ERROR"


def test_multi_two_elem():
    ex(["CLEAR"])
    ex(["PUSH", 10])
    ex(["PUSH", 100])
    act = ex(["*"])
    assert act == [1000]


def test_add_two_elem():
    ex(["CLEAR"])
    ex(["PUSH", 10])
    ex(["PUSH", 100])
    act = ex(["+"])
    assert act == [110]
