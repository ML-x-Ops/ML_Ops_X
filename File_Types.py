class Exports: 
    def export(self,file): 
        raise NotImplementedError("Subclasses must implement this method.") 

class PNG(Exports): 
    def export(self,file): 
        return f"Your file have been successfully downloaded as {file}" 

class PDF(Exports): 
    def export(self,file): 
        return f"Your file have been successfully downloaded as {file}" 
    
class JPG(Exports): 
    def export(self,file): return f"Your file have been successfully downloaded as {file}" 

export_type = {"png":PNG, "pdf":PDF, "jpg":JPG} 

user_input = input("Enter the type of file you need to download: ").lower() 

try: 

    export_class = export_type[user_input]() 

    print(export_class.export(user_input)) 

except KeyError: 
    
    print("Sorry please enter the valid type of file you need to download.")