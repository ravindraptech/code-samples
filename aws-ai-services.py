import boto3

# From Audio to Text with Amazon Transcribe
transcribe = boto3.client('transcribe')

transcribe.start_transcription_job(
  TranscriptionJobName='transcribe-demo',
  Media={'MediaFileUri': 's3://mybucket/transcribe-sample.mp3'},
  MediaFormat='mp3',
  LanguageCode='en-US'
)


# Translation with Amazon Translate, take raw text and turn it into Spanish
translate = boto3.client('translate')

my_phrase = """
Machine learning is employed in a range of computing tasks where designing and programming explicit algorithms with good performance is difficult or infeasible. Example applications include email filtering, detection of network intruders, and computer vision. Machine learning is closely related to computational statistics, which also focuses on predictions making through the use of computer. It has strong ties to mathematical optimization, which delivers methods, theory, and application domains to the field.
"""

response = translate.translate_text(
      Text=my_phrase,
      SourceLanguageCode='auto',
      TargetLanguageCode='es'
  )

print(response['TranslatedText'])

# From Text to Speech with Amazon Polly
polly = boto3.client('polly')

my_text = 'El aprendizaje automático se emplea en una variedad de tareas informáticas en las que diseñar y programar algoritmos explícitos con un buen rendimiento es difícil o inviable. Algunos ejemplos de aplicaciones son el filtrado del correo electrónico, la detección de intrusos en la red y la visión artificial. El aprendizaje automático está estrechamente relacionado con las estadísticas computacionales, que también se centran en la realización de predicciones mediante el uso de la computadora. Tiene fuertes vínculos con la optimización matemática, que aporta métodos, teorías y dominios de aplicación al campo.'

response = polly.synthesize_speech(
    Text=my_text,
    OutputFormat='mp3',
    VoiceId='Lupe',
    LanguageCode='es-MX')

with open('voz.mp3', 'wb') as f:
    f.write(response['AudioStream'].read())


# Sentiment Analysis with Amazon Comprehend, analyze text to understand sentiment (positive, negative, neutral) and detect key entities (names, places, etc.).
comprehend = boto3.client('comprehend')

my_text = 'I love taking photos'

response1=comprehend.detect_sentiment(
    Text=my_text,
    LanguageCode='es'
)
print(response1['Sentiment'])

response2 = comprehend.detect_entities(
    Text=my_text,
    LanguageCode='es'
)
print(response2['Entities'])


# Extracting Text from Documents with Amazon Textract, the optical character recognition (OCR) service that lets you extract text, structured data, and tables from scanned documents or images
textract = boto3.client('textract')

response = textract.detect_document_text(
    Document={'S3Object': {'Bucket': 'mybucket', 
                           'Name': 'note.jpeg'}}
)

for block in response['Blocks']:
    if block['BlockType'] == 'LINE':
        print(block['Text'])


# Image Analysis with Amazon Rekognition
rekognition = boto3.client('rekognition')

response = rekognition.detect_labels(
    Image={'S3Object': {
        'Bucket': 'mybucket', 
        'Name': 'picture.jpeg'
    }},
    MaxLabels=10
)

for label in response['Labels']:
    print(label['Name'], label['Confidence'])


# ref: https://builder.aws.com/content/2rESNvTlHdLY1uMigQeka6MG1n6/building-ai-solutions-on-aws-as-if-they-were-lego-blocks
'''
Transcribe + Translate → multilingual subtitling.
Polly + Comprehend → virtual assistants that speak and understand emotions.
Textract + Rekognition → automated document processing and image analysis.
'''
