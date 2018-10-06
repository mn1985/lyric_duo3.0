from mutagen.id3 import ID3, USLT, ID3NoHeaderError
from mutagen.mp3 import MP3
import codecs
lines = codecs.open("duo.csv", "r", "shift_jis").readlines()

for i in range(560):
    print(i+1)
    lyric = lines[2*i]+lines[2*i+1]
    print(lyric)
    if 1 <= i + 1 <= 100:
        fname='DUO 3.0 CD基礎用 [Disc 1]/DUO基礎/英文01/英文01_'+str('{0:03d}'.format(i+1))+'.mp3'
    elif 101 <= i + 1 <= 211:
        fname='DUO 3.0 CD基礎用 [Disc 2]/DUO基礎/英文01/英文01_'+str('{0:03d}'.format(i+1))+'.mp3'
    elif 212 <= i + 1 <= 328:
        fname='DUO 3.0 CD基礎用 [Disc 3]/DUO基礎/英文01/英文01_'+str('{0:03d}'.format(i+1))+'.mp3'
    elif 329 <= i + 1 <= 448:
        fname='DUO 3.0 CD基礎用 [Disc 4]/DUO基礎/英文01/英文01_'+str('{0:03d}'.format(i+1))+'.mp3'
    elif 449 <= i + 1 <= 560:
        fname='DUO 3.0 CD基礎用 [Disc 5]/DUO基礎/英文01/英文01_'+str('{0:03d}'.format(i+1))+'.mp3'
    try:
        tags = ID3(fname)
    except ID3NoHeaderError:
        print('Adding ID3 header;')
        tags = ID3()
    tags[u"USLT::'eng'"] = USLT(encoding=3, lang=u"eng", desc=u"desc", text=lyric) # lyrics
    tags.save(fname)