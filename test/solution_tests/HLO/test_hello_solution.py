from lib.solutions.HLO.hello_solution import HelloSolution


class TestHello:
    def test_hello(self):
        assert HelloSolution().hello("World") == "Hello World!"
        assert HelloSolution().hello("Joe") == "Hello Joe!"
