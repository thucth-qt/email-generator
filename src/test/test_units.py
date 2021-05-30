import unittest
from src.main.main import get_parser
from src.main.utils.email_generator import *

class TestEmail(unittest.TestCase):
    def testParser(self):
        args = get_parser().parse_args()
        
        self.assertNotEquals(args.template,'')
        self.assertNotEquals(args.customer_infos,'')
        self.assertNotEquals(args.output,'')
        self.assertNotEquals(args.output_error,'')

    def testCheckValid(self):
        row = {'NAME':'Andy', 'PHONE':None}
        not_null_list1=['PHONE']
        not_null_list2=['NAME']

        self.assertFalse(check_valid(row, not_null_list1))
        self.assertTrue(check_valid(row, not_null_list2))

if __name__ == '__main__':
    unittest.main()