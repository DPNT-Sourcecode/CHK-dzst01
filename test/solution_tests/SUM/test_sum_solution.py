from solutions.SUM.sum_solution import SumSolution


class TestSum:
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3
        assert SumSolution().compute(2, 2) == 4
        assert SumSolution().compute(100, 100) == 200
        assert SumSolution().compute(48, 2) == 50
        assert SumSolution().compute(1, 99) == 100

