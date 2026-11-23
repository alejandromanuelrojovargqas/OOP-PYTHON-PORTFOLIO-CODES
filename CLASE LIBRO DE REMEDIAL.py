class book:
    def __init__(self,title,num_pages):
        self.title = title
        self.num_pages = num_pages

        def __str__():
            print(f"book: {self.title}, pages: {self.num_pages}")


        def __len__():
            return f"{num_pages}"

class Ebook:
    def __init__(self,title,num_pages,file_size):
        super().__init__()
        self.file_size = file_size

        def __str__():
            print(f"book: {title}, pages: {num_pages} file_size {file_size}")


book1 = book("don quijote",99)
book2 = Ebook("principito",103,85)
book1.__str__()
book1.__len__()