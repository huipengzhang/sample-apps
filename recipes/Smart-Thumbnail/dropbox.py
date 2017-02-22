import Algorithmia


#Set your Algorithmia API Key
apiKey = 'YOUR API KEY GOES HERE'

# get your API key at algorithmia.com/user#credentials
client = Algorithmia.client(apiKey)

#Pick Algorithm to use
algo = client.algo('opencv/SmartThumbnail/1.0.4')

#Set folder URI path
uri = "dropbox://Camera Uploads"

#Iterate over the Dropbox folder containing images
for f in client.dir(uri).list():
	
	#Check file type is an image
	if f.getName().lower().endswith(('.png','.jpg','.jpeg','.bmp','.gif')):
		#Image progress write
		print "Reading " + f.getName()

		#Define input for Algorithm + Parameters 
		input = [uri + '/' + f.getName(), uri + '/thumbnail_' + f.getName(), 300, 300, "FALSE"]
		
		#Call Algorithm
		output = algo.pipe(input)
		
		print "Thumbnailing: thumbnail_" + f.getName()
       
	else:
		print "File:" + f.getName() +  "is not a type that is supported."

print "Done processing..."