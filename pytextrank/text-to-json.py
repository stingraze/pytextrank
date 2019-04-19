from glob import glob
import argparse, json, re
#All Code from: Used for making json from text.
#https://github.com/satendrapandeymp/pytextrank/blob/master/ttJson.py
WORD = re.compile(r'[\w\.]+')

def ttJson(name, directory=False):
    if directory:
        name = glob(name + "/*.txt")
    else:
        name = [name]
    for ids, fname in enumerate(name):
        with open("".join(fname.split(".")[:-1]) + ".json", 'w') as writer:
            text = open(fname, 'r').read()
            text = " ".join(WORD.findall(text))
            out = '{ "id" : \"' + str(ids+100) + '\", "text": \"' + text + '\"}'  
            writer.write(out)
    print "Done with converting"

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--dir", type=str, help='please type the name of the directory which have your .txt file : \
                            python cnv.py -d "temp dir"')

    parser.add_argument("-f", "--file", type=str, help='please type the name of the file which have want to convert into json : \
                            python cnv.py -f "tempfile.txt"')

    parser.add_argument("-c", "--clear", type=int, choices=[0,1], default=0, help="You want to delete all of the \
                            .txt file , 0 for yes, 1 for no")

    args = parser.parse_args()

    if args.dir:
        ttJson(args.dir, directory=True)

    if args.file:
        ttJson(args.file)

