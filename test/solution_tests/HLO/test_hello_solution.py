from solutions.HLO.hello_solution import HelloSolution


class TestHello:
    def test_hello(self):
        assert HelloSolution().compute("World") == "Hello World!"
        assert HelloSolution().compute("Joe") == "Hello Joe!"
