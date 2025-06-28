class WhatsApp:
    def file(self, data):
        raise NotImplementedError()

class Image(WhatsApp):
    def file(self, data):
        print("This is a Image file")
        
class Video(WhatsApp):
    def file(self, data):
        print("This is a Video file")
        
class Docs(WhatsApp):
    def file(self, data):
        print("This is a Video file")
        
class FactoryFile:
    @staticmethod
    def find_format(format):
        if format == 'image':
            return Image()
        elif format == 'video':
            return Video()
        elif format == 'docs':
            return Docs()
        else:
            raise ValueError("Unsupported format")

file = FactoryFile.find_format("image")
file.file("logo.png")