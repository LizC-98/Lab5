import boto3
#s3_client = boto3.client('s3')
#s3_resource = boto3.resource('s3')

class HTMLDocument:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Message: {self.message}"
    
class HTMLManager:
    def __init__(self):
        self.document = None

    def add_html(self):

        message = """<html>
        <head></head>
        <body><p>Hello World!</p></body>
        </html>"""

        new_docu = HTMLDocument(message)
        self.document = new_docu

    def save_file(self):
        with open("Liz_html_file.html","w") as file:
            file.write(self.document.message)

class AWSManager:  
    def __init__(self):
        self.client = boto3.client('s3')
        self.resource = boto3.resource('s3')
    def listBucketFile(self, bucketName):
        bucket = self.resource.Bucket(bucketName)
        files = bucket.objects.all()
        for file in files:
            print(file.key)

    def save_to_s3(self):
        boto3.client('s3').upload_file('Liz_html_file.html', 'lmtd-class', 'Liz_html_file.html')



manager = HTMLManager()

manager.add_html()

manager.save_file()

my_aws = AWSManager()

#my_aws.save_to_s3()

my_aws.listBucketFile("lmtd-class")

