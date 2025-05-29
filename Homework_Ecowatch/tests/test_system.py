import unittest
from datetime import datetime, timedelta
from logs import Log, parse_csv_logs
from cache import TemporalCache

class TestLogParsing(unittest.TestCase):
    def test_parse_valid_log(self):
        line = "2025-05-29T12:00:00,Sala_1,NORMAL,22.5,45,800,Todo bien"
        with open('temp_test.csv', 'w') as f:
            f.write("timestamp,sala,estado,temperatura,humedad,co2,mensaje\n")
            f.write(line + "\n")
        logs = parse_csv_logs('temp_test.csv')
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0].sala, "Sala_1")
        self.assertAlmostEqual(logs[0].temperatura, 22.5)

    def test_parse_malformed_log(self):
        line = "2025-05-29T12:00:00,Sala_1,NORMAL,XX,45,800,Mensaje"
        with open('temp_test.csv', 'w') as f:
            f.write("timestamp,sala,estado,temperatura,humedad,co2,mensaje\n")
            f.write(line + "\n")
        logs = parse_csv_logs('temp_test.csv')
        self.assertEqual(len(logs), 0)

if __name__ == '__main__':
    unittest.main()
