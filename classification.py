from __future__ import division
import neuro
import sys
import numpy as np
import nltk
import random

result = ['Washington', 0.15806704830805712, 0.14057210230069447, 0.13850949022019596, 0.1297878621101418, 0.1297878621101418, 0.13048045453825396, 0.13097902914051043, 0.12961526727979994, 0.13385452405922, 0.13385452405922, 0.13307949699504754, 0.13307949699504754, 0.12315781062325566, 'Republican'],['Adams', 0.21209497403125002, 0.146791456717472, 0.1348418612068143, 0.1341542954536791, 0.1341542954536791, 0.1351437532174152, 0.13562642878710118, 0.13797398647387343, 0.13557820644934793, 0.13557820644934793, 0.13671960819467466, 0.13830774926413997, 0.13003665890887792, 'Democrat'],['Jefferson', 0.13906459369013752, 0.12613497671836774, 0.1394545487783138, 0.13854689192031747, 0.13854689192031747, 0.13845939362236726, 0.13829749674975214, 0.13559741568607028, 0.13762494483948523, 0.13762494483948523, 0.13654880522634033, 0.13654880522634033, 0.13074402688963205, 'Republican'],['Madison', 0.1353686928158875, 0.08613056263076735, 0.08902676814330646, 0.08324697168334003, 0.08324697168334003, 0.08300823146223685, 0.08282065432193408, 0.07872802173211567, 0.08157150510872659, 0.08157150510872659, 0.08225492457929724, 0.08225492457929724, 0.07816463180369992, 'Republican'],['Monroe', 0.164022117101775, 0.12429779461194919, 0.12334680297560008, 0.1166983568952414, 0.1166983568952414, 0.11651316479739644, 0.11651316479739644, 0.11517666731575726, 0.11631104524626586, 0.11631104524626586, 0.11288634125837382, 0.1139399265472098, 0.11138378462657472, 'Republican'],['Adams', 0.18232253941275, 0.14002266920449769, 0.1384456220891716, 0.1366519897234196, 0.1366519897234196, 0.13838179276755994, 0.14019897710527437, 0.14148940396382959, 0.14507602466589342, 0.14507602466589342, 0.14552918075310356, 0.1459228256504957, 0.1454085039060034, 'Republican'],['Jackson', 0.15542548602225, 0.10711178717083596, 0.1093956886563381, 0.10879571128455871, 0.10879571128455871, 0.1080118593675979, 0.10799338663607885, 0.10983152499161841, 0.11003015172596291, 0.11003015172596291, 0.11116037298225416, 0.11111416557826952, 0.1067918406609919, 'Democrat'],['Buren', 0.132953473379325, 0.05938432335118227, 0.05867186244791156, 0.06067372052978419, 0.06067372052978419, 0.061490447509261914, 0.06146511639191944, 0.06373230962505506, 0.06753066173675198, 0.06753066173675198, 0.06750135558425184, 0.06750135558425184, 0.06667451422334557, 'Democrat'],['Tyler', 0.130493677754, 0.07866069613276756, 0.10255001586672985, 0.10503269341562538, 0.10503269341562538, 0.10279504140374798, 0.10279504140374798, 0.10259011495787003, 0.1046760694429676, 0.1046760694429676, 0.10454271662665172, 0.10454271662665172, 0.10329277194262548, 'Republican'],['Polk', 0.11432348739647501, 0.05891876455930105, 0.05645580392475821, 0.053048533289291336, 0.053048533289291336, 0.051026557608296136, 0.05185955811028199, 0.05416518832542533, 0.056673369829604386, 0.056673369829604386, 0.05716741835570768, 0.057578979405126886, 0.05861991924021568, 'Democrat'],['Taylor', 0.206341190984, 0.054417643195568924, 0.06396631522540082, 0.06648067240363324, 0.06648067240363324, 0.06618693198552505, 0.06627149959689546, 0.06920847708602533, 0.07130830675301734, 0.07130830675301734, 0.0685916365882552, 0.0685916365882552, 0.06467545723525447, 'Republican'],['Fillmore', 0.134191371372, 0.1410308325628726, 0.14211994580246481, 0.13771232947958564, 0.13771232947958564, 0.13907747591005257, 0.13907747591005257, 0.13753095996140477, 0.14141728331141526, 0.14141728331141526, 0.14180150368064257, 0.14180150368064257, 0.1331233513163719, 'Republican'],['Pierce', 0.10234482116417501, 0.09486849621562893, 0.09631309071896071, 0.09492007709403656, 0.09492007709403656, 0.09231328305804572, 0.0925983681693672, 0.09298901903184173, 0.0962187483869508, 0.0962187483869508, 0.09402663946774083, 0.09619264202460434, 0.09677808067376824, 'Democrat'],['Buchanan', 0.080774307162, 0.057087721290086706, 0.05711593563590418, 0.0554491814500883, 0.0554491814500883, 0.05457965518624344, 0.0550146325371781, 0.061475080803512765, 0.06547029684800491, 0.06547029684800491, 0.06313298480102557, 0.06563619374668143, 0.06238471655513865, 'Democrat'],['Lincoln', 0.120742673706425, 0.10756356869120193, 0.10988199359294831, 0.10431013301602292, 0.10431013301602292, 0.10429475319371898, 0.10352480249815851, 0.10312021867371948, 0.1078207301972271, 0.1078207301972271, 0.10630644987604318, 0.1068281187225192, 0.10505399411522909, 'Republican'],['Johnson', 0.13419443648465001, 0.07238472204546995, 0.08234197777575292, 0.07271479114216593, 0.07271479114216593, 0.07064677658989599, 0.07064677658989599, 0.07270928983048949, 0.07790529759745528, 0.07790529759745528, 0.07892491039775412, 0.07904978285685164, 0.07483905459764327, 'Republican'],['Grant', 0.15702013155199998, 0.11977913354519425, 0.12047825428626369, 0.11452097140410238, 0.11452097140410238, 0.11631958494586711, 0.11824053289038654, 0.1220016337440421, 0.12543097499063624, 0.12543097499063624, 0.12448676310134113, 0.12471693283451862, 0.11869135305870374, 'Republican'],['Hayes', 0.18815245335375003, 0.14303349337011034, 0.13830745284075624, 0.13418595214687176, 0.13418595214687176, 0.13230603689539033, 0.13406559201922624, 0.13501023368391846, 0.14377967922532595, 0.14377967922532595, 0.14292364565128007, 0.14294157684627937, 0.1407538915523109, 'Republican'],['Arthur', 0.173590691052, 0.13166491703491764, 0.14036788668941003, 0.13788485252447727, 0.13788485252447727, 0.13756590805833496, 0.13876518573134472, 0.14478633769994817, 0.147530057210209, 0.14760633890924332, 0.14642553172994466, 0.1466149662219833, 0.1398955929832488, 'Republican'],['Cleveland', 0.12306158579285, 0.11823543592002599, 0.11016033751883743, 0.1079692181594464, 0.1079692181594464, 0.1074859318192408, 0.10686572111487684, 0.10735676845403666, 0.1126879492688895, 0.11269612811553127, 0.11354331492905645, 0.11359304596942021, 0.10906633596029218, 'Democrat'],['Harrison', 0.15313989274825002, 0.13956128084467148, 0.13800008585444928, 0.13356768751216577, 0.13356768751216577, 0.1281589472758723, 0.12754643785175068, 0.1266190586230153, 0.1309472194527866, 0.1309472194527866, 0.12532056090994734, 0.12571767128289646, 0.11521147510557848, 'Republican'],['Cleveland', 0.112470351283575, 0.10089253453058486, 0.09716039504285093, 0.09767036303180875, 0.09767036303180875, 0.10288730335571361, 0.1025267636186808, 0.10275645676968485, 0.10579667016742453, 0.10580150603987867, 0.10312833719255743, 0.10303324979303441, 0.09797262491237282, 'Democrat'],['McKinley', 0.1586442503565, 0.09541090321097068, 0.09555913191487769, 0.09279002057302327, 0.09279002057302327, 0.09507320872515572, 0.09569327151166987, 0.09694229075861585, 0.09996039887699074, 0.0999306763476834, 0.09923631100329741, 0.09931222537605147, 0.09544838554772456, 'Republican'],['Roosevelt', 0.08079049732488751, 0.09979388894075991, 0.09901628700947446, 0.09507557603493028, 0.09492419504716418, 0.09333951916300973, 0.09375767553957544, 0.09526115162303567, 0.09826992709245853, 0.09817048916662174, 0.09602036975809558, 0.09517584190446901, 0.0891060945932875, 'Republican'],['Taft', 0.18123135683975, 0.13427432490255772, 0.1377784346108213, 0.13414882304998227, 0.13414882304998227, 0.13585488706290866, 0.13679569496398153, 0.14022377773845077, 0.14208649074282145, 0.14214791158434345, 0.1396639564392988, 0.1396639564392988, 0.13526095236607127, 'Republican'],['Wilson', 0.1363394535256375, 0.11966028256577889, 0.11668569750446627, 0.11019988265541739, 0.11019988265541739, 0.10832374610367039, 0.1081348810321921, 0.1096011840846507, 0.10986877392442138, 0.10986877392442138, 0.1094031959897212, 0.10921080111972425, 0.10899267161466855, 'Democrat'],['Harding', 0.0854329971034, 0.12869363147117469, 0.12297494271989073, 0.1168036983521378, 0.1168036983521378, 0.11830883359825103, 0.11818768989467107, 0.11917024998034628, 0.12183305439106845, 0.12183305439106845, 0.12473419472172612, 0.12473419472172612, 0.12810475565233106, 'Republican'],['Coolidge', 0.1809112277863333, 0.13522616835037887, 0.1282308340331405, 0.12527630711260077, 0.12527630711260077, 0.1281366503257137, 0.12881176759857493, 0.12767316786937064, 0.12996033793447723, 0.12963065821154854, 0.12905028598295118, 0.12926137531890666, 0.1262832608360512, 'Republican'],['Hoover', 0.143306123828725, 0.12168128472785922, 0.10960071760904988, 0.11049579550523812, 0.11049579550523812, 0.11110478956167215, 0.11207253491386783, 0.11168187320442029, 0.11387891569018406, 0.11409057249129176, 0.11585996356752032, 0.11642787229739822, 0.11217391621332738, 'Republican'],['Roosevelt', 0.0926098066312117, 0.07286238992730336, 0.06916735329438352, 0.06542547755797751, 0.06542547755797751, 0.06925030306139336, 0.06963332828034478, 0.06767025206923684, 0.06743110943207875, 0.06738436906189842, 0.06784876946614302, 0.06840385933827833, 0.06705851928117118, 'Democrat'],['Truman', 0.1479528157208125, 0.1245441448944561, 0.12974975523272228, 0.12261768705802717, 0.12261768705802717, 0.12516029985322488, 0.12542577911054303, 0.12711246285961464, 0.1325346748243584, 0.1322193120401448, 0.13129500730016364, 0.13206094762753262, 0.13189656296569857, 'Democrat'],['Eisenhower', 0.18358501487677775, 0.15584407636635736, 0.15515245050128765, 0.15748704628450402, 0.15748704628450402, 0.15972371044603328, 0.15916779126369618, 0.15840777369883027, 0.163420513510975, 0.16340317431261175, 0.16289392565573657, 0.16376437147401762, 0.16259247552525927, 'Republican'],['Kennedy', 0.10782908982553334, 0.11763311323669118, 0.12184398189112888, 0.11824082146578317, 0.11824082146578317, 0.120396691779544, 0.12283367697513153, 0.1227037955870869, 0.12419945228021305, 0.12444056794998933, 0.12395990328725903, 0.12438058148379327, 0.12298841991783223, 'Democrat'],['Johnson', 0.13691182003951666, 0.10041739737112294, 0.09997905204755851, 0.09558220494686148, 0.09558220494686148, 0.10639439631093994, 0.11087516697948491, 0.11038876384046518, 0.11584106718399705, 0.11569520867867299, 0.11666015665116936, 0.1164324435729192, 0.11553312279263106, 'Democrat'],['Nixon', 0.1897865929526, 0.12910144892094716, 0.12394578641616796, 0.12167278119481861, 0.12167278119481861, 0.12750743286748017, 0.12494106372120546, 0.12883784261520503, 0.13581640445252235, 0.13581640445252235, 0.1326641185458261, 0.13338977555933934, 0.13061981873505918, 'Republican'],['Ford', 0.13489606261533335, 0.11838607988272365, 0.11548373558502158, 0.10762820551301912, 0.10762820551301912, 0.11957468670723621, 0.12108568074747024, 0.1228911456574805, 0.12639337982631405, 0.126684144120482, 0.12613674085244073, 0.12564033486098525, 0.11744944783013811, 'Republican'],['Carter', 0.16347857417675002, 0.12244361001923534, 0.11608392431057978, 0.11816306361818377, 0.11768272583494319, 0.12373937635705565, 0.12353569540067774, 0.12467544775572559, 0.12504550081062651, 0.12642218695951946, 0.1272833210501069, 0.12736217248519022, 0.12846510615366857, 'Democrat'],['Reagan', 0.1683488413732143, 0.1333854268070662, 0.12268584520558565, 0.13284042435377483, 0.13262913961372796, 0.13470418576914928, 0.13526509117654736, 0.13648441329425492, 0.13731992782574162, 0.13716973127645568, 0.1370227483848446, 0.13685504578440208, 0.13423696185266676, 'Republican'],['Bush', 0.1340853948691, 0.1302164475371004, 0.13079766376531318, 0.13296404930509467, 0.13296404930509467, 0.13743239837292998, 0.13949090904366207, 0.14036831555702362, 0.1434021113795079, 0.14341784426710505, 0.14306495549111073, 0.14278963481416337, 0.14030583896785492, 'Republican'],['Clinton', 0.12534365592227498, 0.10331300818728774, 0.1038250586834537, 0.09994995412587875, 0.09794962852390504, 0.1035622580316787, 0.10811037839325888, 0.10782500300127533, 0.10960115164150155, 0.10957225451446304, 0.10839854563909823, 0.10807404757497663, 0.10019936352673295, 'Democrat'],['Bush', 0.12807054857903333, 0.08743668744458107, 0.08985850809348724, 0.08021757537231464, 0.0640043230120396, 0.07236878586022522, 0.07280545178728087, 0.07059441880871696, 0.07387521964995401, 0.07371521480058264, 0.07309216611303451, 0.07406713101164847, 0.0728861080130223, 'Republican'],['Obama', 0.11061217749279999, 0.08743668744458107, 0.08985850809348724, 0.08021757537231464, 0.0640043230120396, 0.07236878586022522, 0.07280545178728087, 0.07059441880871696, 0.07387521964995401, 0.07371521480058264, 0.07309216611303451, 0.07406713101164847, 0.0728861080130223, 'Democrat']

def score_features(score):
    features = {}
    features['overall'] = score[0]
    features['government'] = score[1]
    features['economy'] = score[2]
    features['war'] = score[3]
    features['terrorism'] = score[4]
    features['jobs'] = score[5]
    features['education'] = score[6]
    features['foreign'] = score[7]
    features['environment'] = score[8]
    features['energy'] = score[9]
    features['family'] = score[10]
    features['religion'] = score[11]
    features['crime'] = score[12]
    return features

overall = []
government = []
economy = []
war = []
terrorism = []
jobs = []
education = []
foreign = []
environment = []
energy = []
family = []
religion = []
crime = []
parties = []

for pres in result:
    overall.append(pres[1])
    government.append(pres[2])
    economy.append(pres[3])
    war.append(pres[4])
    terrorism.append(pres[5])
    jobs.append(pres[6])
    education.append(pres[7])
    foreign.append(pres[8])
    environment.append(pres[9])
    energy.append(pres[10])
    family.append(pres[11])
    religion.append(pres[12])
    crime.append(pres[13])
    parties.append(pres[14])

master = [overall, government, economy, war, terrorism, jobs, education, foreign, environment, energy, family, religion, crime]
new_master = []

for array in master:
    old_min = min(array)
    old_range = max(array) - old_min
    new_min = -1
    new_range = 1.98
    array = [float((n - old_min) / old_range * new_range + new_min) for n in array]
    new_master.append(array)

# shuffle_list = list(zip(new_master[0],new_master[1],new_master[2],new_master[3],new_master[4],new_master[5],new_master[6],new_master[7],new_master[8],new_master[9],new_master[10],new_master[11],new_master[12],parties))

labeled_parties = []
all_inputs = []
inputs = []
targets = []
index = 0

# for pres in result:
#     labeled_parties.append(([pres[1],pres[2],pres[3],pres[4],pres[5],pres[6],pres[7],pres[8],pres[9],pres[10],pres[11],pres[12],pres[13]],pres[14]))

# random.shuffle(shuffle_list)
# new_master[0],new_master[1],new_master[2],new_master[3],new_master[4],new_master[5],new_master[6],new_master[7],new_master[8],new_master[9],new_master[10],new_master[11],new_master[12],parties = zip(*shuffle_list)

for index in range(len(overall)):
    labeled_parties.append(([new_master[0][index],new_master[1][index],new_master[2][index],new_master[3][index],new_master[4][index],new_master[5][index],new_master[6][index],new_master[7][index],new_master[8][index],new_master[9][index],new_master[10][index],new_master[11][index],new_master[12][index]],parties[index]))
    all_inputs.append([new_master[0][index],new_master[1][index],new_master[2][index],new_master[3][index],new_master[4][index],new_master[5][index],new_master[6][index],new_master[7][index],new_master[8][index],new_master[9][index],new_master[10][index],new_master[11][index],new_master[12][index]])
    if parties[index] == "Republican":
        value = 0
    elif parties[index] == "Democrat":
        value = 1
    else:
        value = -1
    targets.append([value])

neural_counter = 0
naives_counter = 0
static_inputs = list(all_inputs)

for index in range(len(parties)):
    test_input = all_inputs.pop(index)
    inputs = all_inputs
    all_inputs = list(static_inputs)
    reps = 50
    network = []
    network = neuro.setup_network(inputs)
    neuro.train(network,inputs,targets,reps)

    pred = neuro.predict(network, test_input)

    if (pred >= 0 and pred < 0.5):
        pred = 0
    elif (pred >= 0.5 and pred < 1.0):
        pred = 1
    else:
        pred = -1

    if (pred == 0):
        party_guess = "Republican"
    elif (pred == 1):
        party_guess = "Democrat"
    else:
        party_guess = "error - out of range"

    if party_guess == parties[index]:
        neural_counter = neural_counter + 1
    # print("The network thinks the party is " + party_guess + " and the actual party is " + parties[41])

    # random.shuffle(labeled_parties)
    featuresets = [(score_features(n), party) for (n, party) in labeled_parties]
    test_set = [featuresets.pop(index)]
    train_set = featuresets
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    decision_tree = nltk.DecisionTreeClassifier.train(train_set)
    print(decision_tree.pseudocode(depth=1))
    # print("Index" + str(index))
    if (nltk.classify.accuracy(classifier, test_set) == 1.0):
        naives_counter = naives_counter + 1
        featuresets = []
        train_set = []
        classifier = 0
    else:
        featuresets = []
        train_set = []
        classifier = 0

print("Neural Network Accuracy: " + str(float(neural_counter)/float(len(parties))))
print("Naives Bayes Classifier Accuracy: " + str(float(naives_counter)/float(len(parties))))