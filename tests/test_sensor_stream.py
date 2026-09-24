"""Tests for quilt-perception."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from quilt_perception import SensorStreamSubstrate


class TestSensorStreamSubstrate(unittest.TestCase):

    def test_ingest_valid_frame(self):
        """test_ingest_valid_frame"""
        substrate = SensorStreamSubstrate()
        receipt = substrate.step(
            cell_id="c0",
            payload={"k": "v0"},
            status="ok",
        )
        self.assertIsNotNone(receipt)
        self.assertEqual(receipt.polarity, "ACCEPT")

    def test_classify_normal_reading(self):
        """test_classify_normal_reading"""
        substrate = SensorStreamSubstrate()
        receipt = substrate.step(
            cell_id="c1",
            payload={"k": "v1"},
            status="warn",
        )
        self.assertIsNotNone(receipt)
        self.assertEqual(receipt.polarity, "DRIFT")

    def test_route_to_handlers(self):
        """test_route_to_handlers"""
        substrate = SensorStreamSubstrate()
        receipt = substrate.step(
            cell_id="c2",
            payload={"k": "v2"},
            status="fail",
        )
        self.assertIsNotNone(receipt)
        self.assertEqual(receipt.polarity, "REFUSE")

    def test_summarize_window(self):
        """test_summarize_window"""
        substrate = SensorStreamSubstrate()
        receipt = substrate.step(
            cell_id="c3",
            payload={"k": "v3"},
            status="ok",
        )
        self.assertIsNotNone(receipt)
        self.assertEqual(receipt.polarity, "ACCEPT")

    def test_dead_sensor_handling(self):
        """test_dead_sensor_handling"""
        substrate = SensorStreamSubstrate()
        receipt = substrate.step(
            cell_id="c4",
            payload={"k": "v4"},
            status="warn",
        )
        self.assertIsNotNone(receipt)
        self.assertEqual(receipt.polarity, "DRIFT")

    def test_out_of_bounds_refusal(self):
        """test_out_of_bounds_refusal"""
        substrate = SensorStreamSubstrate()
        receipt = substrate.step(
            cell_id="c5",
            payload={"k": "v5"},
            status="fail",
        )
        self.assertIsNotNone(receipt)
        self.assertEqual(receipt.polarity, "REFUSE")


    def test_chain_intact(self):
        substrate = SensorStreamSubstrate()
        for i in range(5):
            substrate.step(f"c{i}", {"i": i})
        self.assertTrue(substrate.chain_intact())

    def test_chain_broken_detected(self):
        substrate = SensorStreamSubstrate()
        substrate.step("c0", {})
        substrate.last_witness_id = ""  # break the chain
        substrate.step("c1", {})
        self.assertFalse(substrate.chain_intact())

    def test_by_polarity(self):
        substrate = SensorStreamSubstrate()
        substrate.step("c0", {}, "ok")
        substrate.step("c1", {}, "warn")
        substrate.step("c2", {}, "fail")
        counts = substrate.by_polarity()
        self.assertEqual(counts["ACCEPT"], 1)
        self.assertEqual(counts["DRIFT"], 1)
        self.assertEqual(counts["REFUSE"], 1)


if __name__ == "__main__":
    unittest.main()
