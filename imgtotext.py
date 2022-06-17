import easyocr
reader = easyocr.Reader(['en'])

results = reader.readtext('captchanro2.PNG')

text = ""
for i in results:
	text+=i[1]+ "\n"
print(text)

"""def detect_text(path):
    #Detects text in the file
    from google.cloud import vision
    import io,os
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))
        
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))"""
"""from google.cloud import vision
import io,os
def detect_text(path):
    list_name = ""
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    for text in texts:
    	list_name = text.description
    	break
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return list_name
list_name = detect_text('test2.jpg')
list_name = list_name.split("\n")
for i in list_name:
	print(i)"""