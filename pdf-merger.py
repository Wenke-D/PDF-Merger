from os import listdir, path
from PyPDF2 import *
from argparse import ArgumentParser


def parseArg():
    parser = ArgumentParser()
    parser.add_argument("docs", nargs="*", help="PDF to merge, more than 2")
    parser.add_argument("-o", "--out", help="output file name")
    parser.add_argument(
        "-d", "--dir", help="source directory, merging all PDFs in that directory.")

    return parser.parse_args()


def wirte_pdf(docs, out):
    merger = PdfFileMerger()

    for pdf in docs:
        merger.append(pdf)

    merger.write(out)


if __name__ == '__main__':

    args = parseArg()
    out = "out.pdf"
    if args.out != None:
        out = args.out

    targets = []
    if args.dir != None:
        files = listdir(args.dir)
        for f in files:
            filename, ext = path.splitext(f)
            if ext == '.pdf':
                targets.append(f)

    else:
        targets = args.docs

    if len(targets) < 2:
        print("Documents to merge less than 2\nUse -h or --help see more info")
        exit(1)

    print("Merging following files:")
    for f in targets:
        print("|", f)
    wirte_pdf(targets, out)
    print("Output PDF name:", out)
