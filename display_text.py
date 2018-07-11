
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--text",default="No text provided",help="Enter some text here in quotes")
parser.add_argument("--verbose",action='store_true',help="verbose output")

args = parser.parse_args()

if args.verbose == True:
    print('args.text="%s" args.verbose="%s"' % (args.text,args.verbose))
print(args.text)
