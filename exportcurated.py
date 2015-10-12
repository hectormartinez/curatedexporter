import argparse
import sys
import os
import shutil

outpath = "outdata/"

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

def main():
    parser = argparse.ArgumentParser(description="Calculates agreement for a lexical sample project in the TSV format")
    parser.add_argument("--folder",   metavar="FILE", default="indata/")
    args = parser.parse_args()



    annotations = []

    for subdir in listdir_nohidden(args.folder):
        for file in [file for file in listdir_nohidden(os.path.abspath(args.folder+subdir+"/curation"))]: #if file.endswith(".tsv")]:


            #print(os.path.abspath(folder+subdir+"/"+file))
            fullpath = os.path.abspath(args.folder+subdir+"/curation/"+file+"/CURATION_USER.tsv")
            idapath = os.path.abspath(args.folder+subdir+"/annotation/"+file+"/ida.tsv")
            sarapath = os.path.abspath(args.folder+subdir+"/annotation/"+file+"/sara.tsv")
            sussipath = os.path.abspath(args.folder+subdir+"/annotation/"+file+"/sussi.tsv")
            bolettepath = os.path.abspath(args.folder+subdir+"/annotation/"+file+"/bolette.tsv")



            if os.path.exists(fullpath):
                print(file,fullpath,"found")
                shutil.copy(fullpath,outpath+file+".curated.tsv")
            elif os.path.exists(idapath) or os.path.exists(sarapath):
                if os.path.exists(idapath):
                    shutil.copy(idapath,outpath+file+".ida.tsv")
                if os.path.exists(sarapath):
                    shutil.copy(sarapath,outpath+file+".sara.tsv")

            elif os.path.exists(sussipath) or os.path.exists(bolettepath):
                    if os.path.exists(sussipath):
                        shutil.copy(sussipath,outpath+file+".sussi.tsv")
                    if os.path.exists(bolettepath):
                        shutil.copy(bolettepath,outpath+file+".bolette.tsv")






if __name__ == "__main__":
    main()