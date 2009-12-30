inp = r'C:\Documents and Settings\ymeng.DLZCORP\Desktop\Marysville Future Model.inp'
f = open(inp)
TITLES = ['[JUNCTIONS]','[LABELS]', '[VERTICES]','[COORDINATES]',  '[RESERVOIRS]','[TANKS]','[PIPES]', '[PUMPS]', '[VALVES]']

results = {}
title = None
for l in f:

    
    
    if l.strip().upper() in TITLES:
        title = l.strip().upper()
        print title
    elif l.strip()=='':
        pass
    elif l.strip()[0] == ";":
        fields = l.strip()[1:].split()
    else:
        if title:
            section = results.setdefault(title, [])
            values = l.strip().split()
            section.append(dict(zip(fields, values)))
        
        


f.close()



features = {}
for pt in results['[COORDINATES]']:

    pid = pt['Node']
    xy = (pt['X-Coord'],pt['Y-Coord'])
    geom = features.setdefault(pid, [])
    geom.append(xy)


for k, v in features.items():
    pass
    #print k, len(v)

features = {}
for pt in results['[VERTICES]']:


    pid = pt['Link']
    xy = (pt['X-Coord'],pt['Y-Coord'])
    geom = features.setdefault(pid, [])
    geom.append(xy)


for k, v in features.items():
    print k, len(v)
