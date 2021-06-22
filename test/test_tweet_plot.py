import unittest
import os
import pybamm
from bot.tweet_plot import Tweet


class TestTweetPlot(unittest.TestCase):
    def test_tweet_graph(self):
        tweet = Tweet(testing=True, choice=0)

        self.assertIsNone(tweet.media_id)
        self.assertIsInstance(tweet.plot, str)
        assert os.path.exists(tweet.plot)
        self.assertIsNone(tweet.processing_info)
        self.assertIsInstance(tweet.model, pybamm.BaseModel)
        self.assertIsInstance(tweet.parameter_values, pybamm.ParameterValues)
        self.assertIsInstance(tweet.time, list)
        self.assertIsInstance(tweet.chemistry, dict)
        self.assertTrue(
            tweet.solver == "CasADi solver with 'safe' mode"
            or tweet.solver == "CasADi solver with 'fast' mode"
            or tweet.solver == (
                "CasADi solver with 'fast with events' mode"
            )
        )
        self.assertIsInstance(tweet.is_experiment, bool)
        self.assertIsNone(tweet.cycle)
        self.assertIsNone(tweet.number)
        self.assertIsInstance(tweet.is_comparison, bool)
        self.assertIsInstance(tweet.testing, bool)

        tweet.upload_init()

        self.assertIsNotNone(tweet.media_id)

        tweet.upload_append()
        tweet.upload_finalize()

        self.assertIsNotNone(tweet.processing_info)

        tweet.tweet()

        assert not os.path.exists("plot.gif")
        assert not os.path.exists("plot.png")

        tweet = Tweet(testing=True, choice=1)

        self.assertIsNone(tweet.media_id)
        self.assertIsInstance(tweet.plot, str)
        assert os.path.exists(tweet.plot)
        self.assertIsNone(tweet.processing_info)
        self.assertIsInstance(tweet.model, pybamm.BaseModel)
        self.assertIsInstance(tweet.parameter_values, pybamm.ParameterValues)
        self.assertIsNone(tweet.time)
        self.assertIsInstance(tweet.chemistry, dict)
        self.assertTrue(
            tweet.solver == "CasADi solver with 'safe' mode"
            or tweet.solver == "CasADi solver with 'fast' mode"
            or tweet.solver == (
                "CasADi solver with 'fast with events' mode"
            )
        )
        self.assertIsInstance(tweet.is_experiment, bool)
        self.assertTrue(tweet.is_experiment)
        self.assertIsInstance(tweet.cycle, list)
        self.assertIsInstance(tweet.cycle[0], tuple)
        self.assertIsInstance(tweet.number, int)
        self.assertIsInstance(tweet.is_comparison, bool)
        self.assertIsInstance(tweet.testing, bool)

        tweet.upload_init()

        self.assertIsNotNone(tweet.media_id)

        tweet.upload_append()
        tweet.upload_finalize()

        self.assertIsNone(tweet.processing_info)

        tweet.tweet()

        assert not os.path.exists("plot.gif")
        assert not os.path.exists("plot.png")


if __name__ == "__main__":
    unittest.main()
