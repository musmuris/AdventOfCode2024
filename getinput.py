import requests
import argparse
import sys

parser = argparse.ArgumentParser("getinput")
parser.add_argument("day", help="Which day to download", type=int)
parser.add_argument("-y", "--year", help="Which day to download", type=int, default=2024)
parser.add_argument("-s", "--session", help="Session cookie", required=True)
args = parser.parse_args()

args.day
r = requests.get(f"https://adventofcode.com/{args.year}/day/{args.day}/input", cookies= {"session":args.session})
if r.status_code != 200:
    print(f"Error {r.status_code}")
    sys.exit(1)

with open(f"src/bin/inputs/day{args.day}.txt", "wt") as f:
    f.write(r.text)


