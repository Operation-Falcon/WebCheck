import argparse
import sys
from banner.banner import banner_design
from function.function import web_check, web_check_file
banner=banner_design()

parser=argparse.ArgumentParser(description=banner, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-d', '--domain', help="passing the subdomain name to see any web service is rnning", type=str)
parser.add_argument('-f', '--file', help='file containing subdomains')
args=parser.parse_args()



if len(sys.argv) == 3 and sys.argv[2]==args.domain:
    web_check(args.domain)
elif len(sys.argv) == 3 and sys.argv[2]==args.file:
    web_check_file(args.file)