import collatz


def test_collatz_9_19():
    target = 9
    result = 19
    expected = "The collatz steps for {} is {}".format(target, result)
    actual =  collatz.collatz_conjecture(target)
    assert actual == expected

def test_collatz_27_111():
    target = 27
    result = 111
    expected = "The collatz steps for {} is {}".format(target, result)
    actual =  collatz.collatz_conjecture(target)
    assert actual == expected

def test_collatz_871_111():
    target = 871
    result = 178
    expected = "The collatz steps for {} is {}".format(target, result)
    actual =  collatz.collatz_conjecture(target)
    assert actual == expected

def test_collatz_6171_261():
    target = 6171
    result = 261
    expected = "The collatz steps for {} is {}".format(target, result)
    actual =  collatz.collatz_conjecture(target)
    assert actual == expected
