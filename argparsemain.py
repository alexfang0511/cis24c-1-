
import argparse
import helper
parser = argparse.ArgumentParser()

parser.add_argument("--num1",type=int,help = "Enter 1st number.")
parser.add_argument("--num2",type=int,help = "Enter 2nd number.")

args = parser.parse_args()
result = helper.add(args.num1,args.num2)
print("sum:",result)