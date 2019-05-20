from collections import defaultdict

def myDict(document):
    word_count = defaultdict(int)
    
    for word in document:
        if word in word_count:
            word_count[word] += 1
    return word_count


doc = "Justicia Carnea (Acanthaceae), is an upright, evergreen shrub, 3 to 7 feet tall and wide. Justicia Carnea (Acanthaceae), is an upright, evergreen shrub, 3 to 7 feet tall and wide. The aim of the experiment was to investigate the physicochemical properties and fatty acid composition of the leaf-stalk of Justicia Carnea. The leaf-stalk used for this study was obtained at Rumuodumaya in Obio-Akpor, Rivers, Nigeria. The leaf-stalk was diced into bits for 32 hours, after which it was ground into fine powders using an electric blender. A 100g quantity of sample was ground in an electric blender with 400ml of water and filtered in order to obtain a clear filtrate for concentration. After this, it was extracted using a suitable solvent. After this the physicochemical properties was obtained using standard analytical techniques while the fatty acid composition was obtained using GC-MS analysis.From the results, Saponification(SV) was 373.07.14mg/kg; Peroxide value (PV) was 44..20mle1/kg; Acid Value(AV) was 4.215%; Thiobarbituric acid value(TBA) was   1.938  mg/kg; Iodine Value was 33.84; Refractive Index was 1.404; Free Fattty Acid(FFA) value was 2.107; Viscosity Pa.S was 1.774; Density g/m was 0.9914.For the fatty acid components, It contained Oleic Acid(12.494%), Lauric Acid(15.076%), Myristic  Acid	(26.265%), Palmitic Acid (31.318%), Arachidonic Acid (13.033%), Arachidic Acid(1.9327%), Linoleic Acid (0.929%), Linolenic Acid (0.8359%). It also had a moderate level of saturated fatty acid (> 30%). But it contained a high level of mono-unsaturated fatty acids(>44%) which are beneficial to health including omega-3 fatty acids. It was concluded that the plant may be of medicinal value and further pharmacological investigation should be carried out on the plant."
print (myDict(doc))
