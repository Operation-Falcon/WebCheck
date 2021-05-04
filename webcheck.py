import argparse
import sys
from banner.banner import banner_design
from function.function import web_check
banner=banner_design()

parser=argparse.ArgumentParser(description=banner, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-d', '--domain', help="passing the subdomain name to see any web service is rnning", type=str)
args=parser.parse_args()



if len(sys.argv) == 3 and sys.argv[2]==args.domain:
    web_check(args.domain)
