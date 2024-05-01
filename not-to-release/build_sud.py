import os

misc_features = [
"AlignBegin",
"AlignEnd",
"Gloss",
"Idiom",
"InIdiom",
"InTitle",
"Lang",
"LangEnd",
"LangStart",
"PronounType",
"SpaceAfter",
"Subject",
"Title",
"VerbTyp",
]

def parse_misc(m):
  d = dict()
  for feat in m.split("|"):
    e = feat.find('=')
    d[feat[0:e]] = feat[e+1:]
  return d

def build (infile, outfile):
  with open(infile, 'r') as f:
    lines = f.readlines()

  with open(outfile, 'w') as f:
    for line in lines:
      l = line.strip()
      if l == "":
        f.write(l+"\n")
      elif l[0] == "#":
        f.write(l+"\n")
      else:
        fields = line.split("\t")
        feats = parse_misc(fields[9])
        reduced_feats = { k: feats[k] for k in feats if k in misc_features }
        misc = "|".join([f"{k}={reduced_feats[k]}" for k in reduced_feats])
        f.write("\t".join(fields[0:9])+"\t"+misc.strip()+"\n")

if __name__ == "__main__":
  for file in os.listdir("."):
    if file.endswith('.conllu'):
      build (file, os.path.join("..", file))
