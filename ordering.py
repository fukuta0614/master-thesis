import os
texs = [d for d in os.listdir() if d.endswith('.tex') and d[0].isdigit()]

count = 1
for tex in sorted(texs):
    os.rename(tex, str(count) + tex[1:])
    print(str(count) + tex[1:])
    count += 1
