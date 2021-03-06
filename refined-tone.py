from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot
import glob
import re
import nltk
from nltk import *

lexicon = open("sent_lexicon.csv","r")
lexicon = lexicon.read()
lexicon = lexicon.split("\n")
for index in range(len(lexicon)):
    lexicon[index]=lexicon[index].split(",")
    try:
        lexicon[index][1] = np.float32(lexicon[index][1])
    except:
        del(lexicon[index])

common = open("105_common.txt", "r")
common=common.read()
common=common.lower()
common=common.split("\n")

negators = open("negators.txt", "r")
negators = negators.read()
negators = negators.lower()
negators = negators.split("\n")

intensifiers = open("intensifiers.txt", "r")
intensifiers = intensifiers.read()
intensifiers = intensifiers.lower()
intensifiers = intensifiers.split("\n")

averages = [[] for j in range(50)]
names = [[] for j in range(50)]
last_names = []
list_counter = 0
current_last = ""

for filename in sorted(glob.glob('Addresses/*.txt')):
    current_last = filename[17:]
    current_last = current_last.replace('.txt','')
    last_names.append(current_last)
    break

for filename in sorted(glob.glob('Addresses/*.txt')):
    total = 0
    average = 0
    count = 0
    file = open(filename, 'r')
    address = file.read()
    address = address.replace('\r\n', ' ')
    address = address.replace('  ', ' ')
    address = address.lower()
    address = re.sub('[.,\/#!$%\^&\*;:{}=\-_`~()]', '', address)
    address = address.split(" ")

    # bigrams = list(bigrams(address))

    # Count the words in the speech
    ct_dct={}
    ng_dct={}
    int_dct={}
    prev = ''
    for index in range(len(address)):
        word = address[index]
        if index != 0:
            prev = address[index-1]
        try:
            ct_dct[word]=ct_dct[word]+1
        except:
            ct_dct[word]=1
            for neg_index in range(len(negators)):
                if negators[neg_index] == prev:
                    try:
                        ng_dct[word] = ng_dct[word] + 1
                    except:
                        ng_dct[word] = 1
            for int_index in range(len(intensifiers)):
                if intensifiers[int_index] == prev:
                    try:
                        int_dct[word] = int_dct[word] + 1
                    except:
                        int_dct[word] = 1
        else:
            for neg_index in range(len(negators)):
                if negators[neg_index] == prev:
                    try:
                        ng_dct[word] = ng_dct[word] + 1
                    except:
                        ng_dct[word] = 1
            for int_index in range(len(intensifiers)):
                if intensifiers[int_index] == prev:
                    try:
                        int_dct[word] = int_dct[word] + 1
                    except:
                        int_dct[word] = 1

    # Iterate through the dictionary and make sure the word isn't common then check if it's in the lexicon
    # If it is then replace the word with it's sentiment score to give you a list of the sentiment scores and their frequency in the text
    for key, value in ct_dct.items():
        for index in range(len(lexicon)):
            if not key in common:
                if key == lexicon[index][0]:
                    try:
                        ng_dct[key]
                    except:
                        try:
                            int_dct[key]
                        except:
                            total = total + (lexicon[index][1] * value)
                            count = count + value
                            continue
                        else:
                            total = total + (lexicon[index][1] * (2^int_dct[key]) * value)
                            count = count + value
                            continue
                    # since negating one essentially cancels it out you can just subtract from the total number of that term
                    else:
                        for countdown in range(ng_dct[key]):
                            value = value - 1
                        try:
                            int_dct[key]
                        except:
                            total = total + (lexicon[index][1] * value)
                            count = count + value
                            continue
                        else:
                            total = total + (lexicon[index][1] * value)
                            count = count + value
                            continue
                        total = total + (lexicon[index][1] * (2^int_dct[key]) * value)
                        count = count + value
                        continue
                elif key[:len(key)-1] == lexicon[index][0]:
                    try:
                        ng_dct[key[:len(key)-1]]
                    except:
                        try:
                            int_dct[key[:len(key)-1]]
                        except:
                            total = total + (lexicon[index][1] * value)
                            count = count + value
                            continue
                        else:
                            total = total + (lexicon[index][1] * (2^int_dct[key[:len(key)-1]]) * value)
                            count = count + value
                            continue
                    # since negating one essentially cancels it out you can just subtract from the total number of that term
                    else:
                        for countdown in range(ng_dct[key[:len(key)-1]]):
                            value = value - 1
                        try:
                            int_dct[key[:len(key)-1]]
                        except:
                            total = total + (lexicon[index][1] * value)
                            count = count + value
                            continue
                        else:
                            total = total + (lexicon[index][1] * value)
                            count = count + value
                            continue
                        total = total + (lexicon[index][1] * (2^int_dct[key[:len(key)-1]]) * value)
                        count = count + value
                        continue
                elif key[:len(key)-2] == lexicon[index][0]:
                    try:
                        ng_dct[key[:len(key)-2]]
                    except:
                        try:
                            int_dct[key[:len(key)-2]]
                        except:
                            total = total + (lexicon[index][1] * value)
                            count = count + value
                            continue
                        else:
                            total = total + (lexicon[index][1] * (2^int_dct[key[:len(key)-2]]) * value)
                            count = count + value
                            continue
                    # since negating one essentially cancels it out you can just subtract from the total number of that term
                    else:
                        for countdown in range(ng_dct[key[:len(key)-2]]):
                            value = value - 1
                        try:
                            int_dct[key[:len(key)-2]]
                        except:
                            total = total + (lexicon[index][1] * value)
                            count = count + value
                            continue
                        else:
                            total = total + (lexicon[index][1] * value)
                            count = count + value
                            continue
                        total = total + (lexicon[index][1] * (2^int_dct[key[:len(key)-2]]) * value)
                        count = count + value
                        continue
                elif key[:len(key)-3] == lexicon[index][0]:
                    try:
                        ng_dct[key[:len(key)-3]]
                    except:
                        try:
                            int_dct[key[:len(key)-3]]
                        except:
                            total = total + (lexicon[index][1] * value)
                            count = count + value
                            continue
                        else:
                            total = total + (lexicon[index][1] * (2^int_dct[key[:len(key)-3]]) * value)
                            count = count + value
                            continue
                    # since negating one essentially cancels it out you can just subtract from the total number of that term
                    else:
                        for countdown in range(ng_dct[key[:len(key)-3]]):
                            value = value - 1
                        try:
                            int_dct[key[:len(key)-3]]
                        except:
                            total = total + (lexicon[index][1] * value)
                            count = count + value
                            continue
                        else:
                            total = total + (lexicon[index][1] * value)
                            count = count + value
                            continue
                        total = total + (lexicon[index][1] * (2^int_dct[key[:len(key)-3]]) * value)
                        count = count + value
                        continue
                # elif key[:len(key)-1] == lexicon[index][0]:
                #     total = total + (lexicon[index][1] * value)
                #     count = count + value
                #     continue
                # elif key[:len(key)-2] == lexicon[index][0]:
                #     total = total + (lexicon[index][1] * value)
                #     count = count + value
                #     continue
                # elif key[:len(key)-3] == lexicon[index][0]:
                #     total = total + (lexicon[index][1] * value)
                #     count = count + value
                #     continue


    average = total / count
    name = filename[10:16]
    print(filename + " " + str(average))

    last = filename[17:]
    last = last.replace('.txt','')
    if (last != current_last):
        list_counter = list_counter + 1
        current_last = last
        last_names.append(current_last)
    names[list_counter].append(name)
    averages[list_counter].append(average)

print(names)
print(averages)
print(last_names)

# [179001, 179012, 179110, 179211, 179312, 179411, 179512, 179612, 179711, 179812, 179912, 180011, 180112, 180212, 180310, 180411, 180512, 180612, 180710, 180811, 180911, 181012, 181111, 181211, 181312, 181409, 181512, 181612, 181712, 181811, 181912, 182011, 182112, 182212, 182312, 182412, 182512, 182612, 182712, 182812, 182912, 183012, 183112, 183212, 183312, 183412, 183512, 183612, 183712, 183812, 183912, 184012, 184112, 184212, 184312, 184412, 184512, 184612, 184712, 184812, 184912, 185012, 185112, 185212, 185312, 185412, 185512, 185612, 185712, 185812, 185912, 186012, 186112, 186212, 186312, 186412, 186512, 186612, 186712, 186812, 186912, 187012, 187112, 187212, 187312, 187412, 187512, 187612, 187712, 187812, 187912, 188012, 188112, 188212, 188312, 188412, 188512, 188612, 188712, 188812, 188912, 189012, 189112, 189212, 189312, 189412, 189512, 189612, 189712, 189812, 189912, 190012, 190112, 190212, 190312, 190412, 190512, 190612, 190712, 190812, 190912, 191012, 191112, 191212, 191312, 191412, 191512, 191612, 191712, 191812, 191912, 192012, 192112, 192212, 192312, 192412, 192512, 192612, 192712, 192812, 192912, 193012, 193112, 193212, 193401, 193501, 193601, 193701, 193801, 193901, 194001, 194101, 194201, 194301, 194401, 194501, 194601, 194701, 194801, 194901, 195001, 195101, 195201, 195301, 195302, 195401, 195501, 195601, 195701, 195801, 195901, 196001, 196101, 196101, 196201, 196301, 196401, 196501, 196601, 196701, 196801, 196901, 197001, 197101, 197201, 197302, 197401, 197501, 197601, 197701, 197801, 197901, 198001, 198101, 198201, 198301, 198401, 198502, 198602, 198701, 198801, 198902, 199001, 199101, 199201, 199302, 199401, 199501, 199601, 199702, 199801, 199901, 200001, 200102, 200109, 200201, 200301, 200401, 200502, 200601, 200701, 200801, 200902, 201001, 201101, 201201, 201302, 201401, 201501, 201601]

 # [0.32958909436579675, 0.22269439847644315, 0.20516202796941979, 0.17043009070822826, 0.070270161937784265, 0.073039130863553278, 0.20165294172508377, 0.16322058647674087, 0.15059547956073563, 0.17189849573269225, 0.22884885492050541, 0.29703706590966744, 0.16762207196195528, 0.15154447826383946, 0.15265949628697736, 0.11311583391110377, 0.10132362805651846, 0.17141741037296787, 0.094160262055115324, 0.16067356861181023, 0.091103838229796799, 0.1911071785040446, 0.11026829612993561, 0.044009510629860929, 0.081746887115911507, 0.079530187014479808, 0.28813876576803543, 0.19704487913520025, 0.23116355348629966, 0.079504418424239345, 0.13583810873241467, 0.21640256608975686, 0.10843432767658817, 0.18464619990403955, 0.18773821660865889, 0.16844954589203492, 0.19448978941945558, 0.1689157714410979, 0.18074277695375074, 0.18514181983682815, 0.16670985447047595, 0.15158489280140278, 0.1854847985528614, 0.18458952835980655, 0.19889138161778008, 0.11124460701057359, 0.13148162797916976, 0.11341719738638895, 0.17153905556193261, 0.14354129475475205, 0.097319972955280179, 0.11941357024532449, 0.14229740779618827, 0.11752905180864602, 0.1301061402146633, 0.13204211119642073, 0.14898766787114462, 0.10529980452047835, 0.086976916440888216, 0.11602956075377825, 0.20634119098367146, 0.14897820421455399, 0.12170451093486875, 0.13189139896597107, 0.18072311811693567, 0.078586964235094786, 0.056727851257108955, 0.093341351047532245, 0.081018107132230816, 0.097409803534712569, 0.061429044317861066, 0.083240273663229614, 0.13891577514817158, 0.090758128629652213, 0.10725421827968945, 0.14604257276823457, 0.14080555115105972, 0.17731175754774123, 0.099257436780626249, 0.11940300045854157, 0.16529098063295067, 0.15913012606016108, 0.22063078080499657, 0.1865998904876135, 0.1297905656831346, 0.13681356502929704, 0.11640047074469881, 0.14150467297324681, 0.15674272928768257, 0.1753787710500318, 0.17488370552747207, 0.24560460755007893, 0.19597448451903635, 0.17494553472314561, 0.15341635782243615, 0.17002638714446866, 0.12429361486473404, 0.14553759308851497, 0.085365839596414236, 0.13704929562055901, 0.16464570901402781, 0.15820089012685448, 0.12546357669132499, 0.16424939516100953, 0.13762454919130515, 0.096542164183418711, 0.11682005648969844, 0.098894635269882181, 0.12534428806137787, 0.12546351033827025, 0.20239841183370882, 0.18137079119347713, 0.095765866587269252, 0.10134165589961242, 0.12447344436365015, 0.08588665480101941, 0.076312486400897855, 0.047719788127779737, 0.066499740500160442, 0.0483243419178601, 0.19591494848655622, 0.2209963501197672, 0.1462490175302241, 0.1617651112223466, 0.11984774869467531, 0.17904644393584065, 0.1348621572838869, 0.11839527171608565, 0.078236714609061619, 0.14011033041218218, 0.12038602972428454, 0.19983093182866771, 0.094405875011429274, 0.076460119195376777, 0.17759755555362927, 0.17818769482990443, 0.21089157908898123, 0.1829296902303669, 0.14542373493368857, 0.19043711208063982, 0.16367214900851978, 0.099946829577899313, 0.1642796033832975, 0.14532591334483572, 0.15032662186445545, 0.17864657101631165, 0.16181878750908307, 0.15233304310846424, 0.019577414234576422, 0.080799567675256451, 0.095909236383832197, 0.13945026975870131, -0.0077666112362113722, -0.0030779709121495757, 0.075596985377650444, 0.067703764795535998, 0.11394809835005595, 0.12410609546209403, 0.194904411901692, 0.1622770017583266, 0.22790352207599612, 0.1255465274216441, 0.14162030741872203, 0.093316561377455448, 0.18130629724744476, 0.20279186346007946, 0.23761669174104907, 0.17661535728466837, 0.18894710958360911, 0.13246428068574365, 0.19169474062878775, 0.13951757415260435, 0.20131121910580371, 0.080969257858567886, 0.12406104696262121, 0.11845696465495754, 0.092648853422531277, 0.2057866881675928, 0.081283202935611046, 0.13785879536251711, 0.14447253747747529, 0.15942084287117059, 0.12596033585842728, 0.22999062818563637, 0.18200979952812193, 0.22595155201092057, 0.18502064917983604, 0.11346485759773647, 0.13076122833642168, 0.1604621019117379, 0.15403337561631505, 0.18008269187139006, 0.14887223644153252, 0.17092599277803103, 0.078141819966498327, 0.11330584564828185, 0.22558684802372544, 0.21938484875104761, 0.19786156815870193, 0.1652863476575421, 0.17887461140572306, 0.150589587968155, 0.19688274160392219, 0.10524945501944066, 0.083619794885444035, 0.12943546897357569, 0.10259936176105425, 0.089037880939945954, 0.077316301641287985, 0.13755053790244506, 0.16598571123352804, 0.14650880978128758, 0.15431517514464951, 0.1985054606830837, 0.023401832351317771, 0.095300528726253428, 0.0780631713271141, 0.095350466398596095, 0.22394358898060662, 0.14479484180204547, 0.11182471512628983, 0.18145033181644976, 0.073489439962037689, 0.070169735082986698, 0.15102540380525267, 0.071909381658436577, 0.16157822454720736, 0.1398887309060606, 0.10326607794045925, 0.11357042604138394]
