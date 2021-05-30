from src.main.utils import generate_email
import sys
import os
import argparse

def get_parser():
    parser = argparse.ArgumentParser(
        description='Email Generator')
    parser.add_argument(
        '--template',
        default='./email_template/email_template.json',
        help='Path to the FILE contains email template.')

    parser.add_argument(
        '--customer-infos',
        default='./customers_info/customers.csv',
        help='Path to the FILE contains customer informations.')

    parser.add_argument(
        '--output',
        default='./output_emails',
        help='Path to the DIRECTORY of output.')

    parser.add_argument(
        '--output-error',
        default='./output_errors/errors.csv',
        help='Path to the FILE contains error outputs.')

    return parser

if __name__=="__main__":
    args = get_parser().parse_args()
    os.makedirs(args.output,exist_ok=True)
    os.makedirs(os.path.split(args.output_error)[0],exist_ok=True)

    generate_email(args.template, args.customer_infos, args.output+'/email_{}.json', args.output_error)