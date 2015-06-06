#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import csv

#converting latest 10 records from eathquake.csv
record2read = 10

#replacing digits and place to Nepali
reps = {
	'*' : '',
	'1':'१'	,
	'2':'२'	,
	'3':'३'	,
	'4':'४'	,
	'5':'५'	,
	'6':'६'	,
	'7':'७'	,
	'8':'८'	,
	'9':'९'	,
	'0':'०',
	'Local Time' : 'LocalTime',
	'Magnitude(ML)' : 'Magnitude',
	'Achham' : 'अछाम'	,
	'Arghakhanchi' : 'अर्घाखाँची'	,
	'Baglung' : 'बाग्लुङ'	,
	'Baitadi' : 'बैतडी'	,
	'Bajhang' : 'बझाङ'	,
	'Bajura' : 'बाजुरा'	,
	'Banke' : 'बाँके'	,
	'Bara' : 'बारा'	,
	'Bardiya' : 'बर्दिया'	,
	'Bhaktapur' : 'भक्तपुर'	,
	'Bhojpur' : 'भोजपुर'	,
	'Chitwan' : 'चितवन'	,
	'Dadeldhura' : 'डडेल्धुरा'	,
	'Dailekh' : 'दैलेख'	,
	'Dang' : 'दाङ'	,
	'Darchula' : 'दार्चुला'	,
	'Dhading' : 'धादिङ'	,
	'Dhankuta' : 'धनकुटा'	,
	'Dhanusa' : 'धनुषा'	,
	'Dolakha' : 'दोलखा'	,
	'Dolpa' : 'डोल्पा'	,
	'Doti' : 'डोटी'	,
	'Gorkha' : 'गोरखा'	,
	'Gulmi' : 'गुल्मी'	,
	'Humla' : 'हुम्ला'	,
	'Ilam' : 'इलाम'	,
	'Jajarkot' : 'जाजरकोट'	,
	'Jhapa' : 'झापा'	,
	'Jumla' : 'जुम्ला'	,
	'Kailali' : 'कैलाली'	,
	'Kalikot' : 'कालिकोट'	,
	'Kanchanpur' : 'कञ्चनपुर'	,
	'Kapilvastu' : 'कपिलबस्तु'	,
	'Kaski' : 'कास्की'	,
	'Kathmandu' : 'काठमाडौ'	,
	'Kavre' : 'काभ्रे'	,
	'Kavrepalanchok' : 'काभ्रे'	,
	'Khotang' : 'खोटाङ'	,
	'Lalitpur' : 'ललितपुर'	,
	'Lalitput' : 'ललितपुर'	,
	'Lamjung' : 'लमजुङ'	,
	'Mahottari' : 'महोत्तरी'	,
	'Makawanapur' : 'मकवानपुर'	,
	'Makawanpur' : 'मकवानपुर'	,
	'Manang' : 'मनाङ'	,
	'Morang' : 'मोरङ'	,
	'Mugu' : 'मुगु'	,
	'Mustang' : 'मुस्ताङ'	,
	'Myagdi' : 'म्याग्दी'	,
	'Nawalparasi' : 'नवलपरासी'	,
	'Nuwakot' : 'नुवाकोट'	,
	'Okhaldhunga' : 'ओखलढुङ्गा'	,
	'Palpa' : 'पाल्पा'	,
	'Panchthar' : 'पाँचथर'	,
	'Parbat' : 'पर्वत'	,
	'Parsa' : 'पर्सा'	,
	'Pyuthan' : 'प्यूठान'	,
	'Ramechhap' : 'रामेछाप'	,
	'Rasuwa' : 'रसुवा'	,
	'Rautahat' : 'रौतहट'	,
	'Rolpa' : 'रोल्पा'	,
	'Rukum' : 'रुकुम'	,
	'Rupandehi' : 'रुपन्देही'	,
	'Salyan' : 'सल्यान'	,
	'Saptari' : 'सप्तरी'	,
	'Sarlahi' : 'सर्लाही'	,
	'Sankhuwasabha' : 'संखुवासभा'	,
	'Sindhuli' : 'सिन्धुली'	,
	'Sindhupalchok' : 'सिन्धुपाल्चोक'	,
	'Sindhupalchowk' : 'सिन्धुपाल्चोक'	,
	'Sindupalchok' : 'सिन्धुपाल्चोक'	,
	'Siraha' : 'सिराहा'	,
	'Solukhumbu' : 'सोलुखुम्बु'	,
	'Sunsari' : 'सुनसरी'	,
	'Surkhet' : 'सुर्खेत'	,
	'Syangja' : 'स्याङ्जा'	,
	'Tanahu' : 'तनहुँ'	,
	'Taplejung' : 'ताप्लेजुङ'	,
	'Terhathum' : 'तेह्रथुम'	,
	'Udayapur' : 'उदयपुर'	,
	'Tibet' : 'तिब्बत'
	}

# replace text function
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text


# split big array into sub
def split(arr, size):
     arrs = []
     while len(arr) > size:
         piece = arr[:size]
         arrs.append(piece)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs


x = []
with open('earthquake.csv', 'rb') as csvfile:
	earthquake = csv.reader(csvfile, delimiter=',')

	for row in range(record2read):
		
		row = [word.replace(' ','') for word in earthquake.next()]
		row = ' '.join(row).encode('utf-8')
		row = replace_all(row, reps)
		x += str.split(row, " ")
	

#print/save - earthquakene.csv
data = (split(x,11))

x = ""
myfile = open("earthquakenep.csv", "w")
for i in range(record2read):
	x += ', '.join(data[i]) +"\n"

myfile.write(x)