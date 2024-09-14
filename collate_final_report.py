import argparse

parser = argparse.ArgumentParser(prog = 'main', description='collate FinalStats.csv from output of Amaranth run.')
parser.add_argument('directory_name', metavar='source_dir', type=str, nargs=1,
                    help='location of directory where image files used for the run are stored')
parser.add_argument('--prefix', dest='image_prefix', action='store',
                    help='sum the integers (default: find the max)')

args = parser.parse_args()

# print args.directory_name(args.integers)