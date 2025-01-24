# tests/test_hello.py

def test_hello_output(capfd):
    import hello_world
    captured = capfd.readouterr()
    assert captured.out.strip() == "Hello, Ankit!"
