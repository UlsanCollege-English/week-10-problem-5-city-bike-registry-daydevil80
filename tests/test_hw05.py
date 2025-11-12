


import sys, os, random
# ✅ ensure we can import main.py from parent folder
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import HashMap

# ---- Normal tests (4) ----

def test_len_and_basic_put_get():
    m = HashMap(m=4)
    assert len(m) == 0
    m.put("B1", "S1")
    assert len(m) == 1
    assert m.get("B1") == "S1"

def test_overwrite_value():
    m = HashMap()
    m.put("B2", "X")
    m.put("B2", "Y")
    assert len(m) == 1
    assert m.get("B2") == "Y"

def test_delete_present_and_absent():
    m = HashMap()
    m.put("K", "V")
    assert m.delete("K") is True
    assert m.delete("K") is False
    assert m.get("K") is None

def test_many_puts_trigger_resize():
    m = HashMap(m=2)
    for i in range(10):
        m.put(f"id{i}", f"s{i}")
    # should have resized at least once
    assert len(m) == 10
    # spot check
    assert m.get("id0") == "s0"
    assert m.get("id9") == "s9"

# ---- Edge-case tests (3) ----

def test_get_missing_key_returns_none():
    m = HashMap()
    assert m.get("missing") is None

def test_delete_missing_returns_false():
    m = HashMap()
    assert m.delete("ghost") is False

def test_resize_preserves_all_pairs():
    m = HashMap(m=2)
    items = [(f"B{i}", f"S{i}") for i in range(8)]
    for k, v in items:
        m.put(k, v)
    for k, v in items:
        assert m.get(k) == v

# ---- More-complex tests (3) ----

def test_heavy_collisions_still_correct_after_resize():
    m = HashMap(m=2)
    for i in range(50):
        m.put(f"AA{i}", str(i))
    assert len(m) == 50
    for i in range(0, 50, 7):
        assert m.get(f"AA{i}") == str(i)

def test_interleave_put_delete():
    m = HashMap(m=4)
    for i in range(12):
        m.put(f"X{i}", str(i))
        if i % 3 == 0:
            m.delete(f"X{i}")
    for i in range(12):
        v = m.get(f"X{i}")
        if i % 3 == 0:
            assert v is None
        else:
            assert v == str(i)

def test_multiple_resizes_and_integrity():
    m = HashMap(m=1)
    for i in range(40):
        m.put(str(i), str(i))
    for i in range(40):
        assert m.get(str(i)) == str(i)
