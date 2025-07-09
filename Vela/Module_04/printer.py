class NewPrinter:
    def print_document(self, text):
        print(f"Printing document: {text}")

class DotMatrixPrinter:
    def print_dot_matrix(self, text):
        print(f"Dot Matrix printing: {text}")

class DotAdapter:
    def __init__(self, dot_mat):
        self.dot_mat = dot_mat
    
    def print_document(self, text):
        self.dot_mat.print_dot_matrix(text)
    
new = NewPrinter()
dot = DotMatrixPrinter()
dot_adapter = DotAdapter(dot)

dot_adapter.print_document("fuck off")
new.print_document("you fuck off")