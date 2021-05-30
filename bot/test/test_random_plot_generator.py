import unittest
import pybamm
from plotting.random_plot_generator import random_plot_generator


class TestTweetPlot(unittest.TestCase):
    def test_tweet_graph(self):
        (
            model,
            parameter_values,
            time,
            chemistry,
            solver,
            isExperiment,
            cycle,
            number,
            isComparison,
        ) = random_plot_generator(
            testing=True,
            provided_choice=0
        )

        self.assertIsInstance(model, pybamm.BaseBatteryModel)
        self.assertEqual("lithium_ion", chemistry["chemistry"])
        self.assertIsInstance(solver, pybamm.BaseSolver)
        self.assertIsInstance(parameter_values, pybamm.ParameterValues)
        self.assertIsInstance(time, int)
        self.assertIsNone(cycle)
        self.assertIsNone(number)
        self.assertFalse(isExperiment)
        self.assertFalse(isComparison)

        (
            model,
            parameter_values,
            time,
            chemistry,
            solver,
            isExperiment,
            cycle,
            number,
            isComparison,
        ) = random_plot_generator(
            testing=True,
            provided_choice=1
        )

        self.assertIsInstance(model, pybamm.BaseBatteryModel)
        self.assertEqual("lithium_ion", chemistry["chemistry"])
        self.assertIsInstance(solver, pybamm.BaseSolver)
        self.assertIsInstance(parameter_values, pybamm.ParameterValues)
        self.assertIsInstance(time, int)
        self.assertIsNotNone(cycle)
        self.assertIsNotNone(number)
        self.assertTrue(isExperiment)
        self.assertFalse(isComparison)
        pybamm.Experiment(cycle * number)

        (
            models,
            parameter_values,
            time,
            chemistry,
            solver,
            isExperiment,
            cycle,
            number,
            isComparison,
        ) = random_plot_generator(
            testing=True,
            provided_choice=2
        )

        for model in models.values():
            self.assertIsInstance(model, pybamm.BaseBatteryModel)
        self.assertEqual("lithium_ion", chemistry["chemistry"])
        self.assertIsNone(solver)
        self.assertIsInstance(parameter_values, pybamm.ParameterValues)
        self.assertIsInstance(time, int)
        self.assertIsNone(cycle)
        self.assertIsNone(number)
        self.assertFalse(isExperiment)
        self.assertTrue(isComparison)

        (
            models,
            parameter_values,
            time,
            chemistry,
            solver,
            isExperiment,
            cycle,
            number,
            isComparison,
        ) = random_plot_generator(
            testing=True,
            provided_choice=2,
            provided_number_of_comp=1
        )

        for model in models.values():
            self.assertIsInstance(model, pybamm.BaseBatteryModel)
        self.assertEqual("lithium_ion", chemistry["chemistry"])
        self.assertIsNone(solver)
        self.assertIsInstance(parameter_values, pybamm.ParameterValues)
        self.assertIsInstance(time, int)
        self.assertIsNone(cycle)
        self.assertIsNone(number)
        self.assertFalse(isExperiment)
        self.assertTrue(isComparison)


if __name__ == "__main__":
    unittest.main()
