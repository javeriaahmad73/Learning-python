
# Book class
class Book:
    def _init_(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def label(self):
        return f"{self.title} by {self.author} ({self.book_id})"


# Member class
class Member:
    def _init_(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed = set()  # books currently borrowed

    def can_borrow(self, max_loans):
        return len(self.borrowed) < max_loans


# Library class
class Library:
    def _init_(self, max_loans=3):
        self.max_loans = max_loans
        self.books = {}    # book_id -> Book
        self.members = {}  # member_id -> Member
        self.loans = {}    # book_id -> (member_id, due_days)

    def add_book(self, book):
        if book.book_id in self.books:
            print(f"Book {book.book_id} already exists!")
        else:
            self.books[book.book_id] = book

    def register_member(self, member):
        if member.member_id in self.members:
            print(f"Member {member.member_id} already exists!")
        else:
            self.members[member.member_id] = member

    def borrow(self, book_id, member_id, due_days=14):
        if book_id not in self.books:
            print("Book not found.")
            return
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id in self.loans:
            print("Book is already borrowed.")
            return

        member = self.members[member_id]
        if not member.can_borrow(self.max_loans):
            print("Member reached max loan limit.")
            return

        # Borrow the book
        self.loans[book_id] = (member_id, due_days)
        member.borrowed.add(book_id)
        print(f"{member.name} borrowed {self.books[book_id].title} for {due_days} days.")

    def return_book(self, book_id):
        if book_id not in self.loans:
            print("This book is not borrowed.")
            return
        member_id, _ = self.loans.pop(book_id)
        self.members[member_id].borrowed.remove(book_id)
        print(f"{self.books[book_id].title} returned successfully.")

    def list_available(self):
        print("Available books:")
        for book_id, book in self.books.items():
            if book_id not in self.loans:
                print("-", book.label())

    def member_loans(self, member_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        print(f"{member.name}'s borrowed books:")
        for book_id in member.borrowed:
            _, due = self.loans[book_id]
            print(f"- {self.books[book_id].label()}, due in {due} days")


# ------------------------------
# Example usage
# ------------------------------

if __name__ == "_main_":
    lib = Library(max_loans=2)

    # Add books
    lib.add_book(Book("B001", "Clean Code", "Robert C. Martin"))
    lib.add_book(Book("B002", "Python Crash Course", "Eric Matthes"))
    lib.add_book(Book("B003", "The Pragmatic Programmer", "Andrew Hunt"))

    # Register members
    lib.register_member(Member("M001", "Ayesha"))
    lib.register_member(Member("M002", "Hassan"))

    # Borrow books
    lib.borrow("B001", "M001", due_days=7)
    lib.borrow("B002", "M001")

    # List available books
    lib.list_available()

    # Show member loans
    lib.member_loans("M001")

    # Return a book
    lib.return_book("B001")
    lib.list_available()# class A:
#     varA="welcome to class A"

# class B:
#     varB="welcome to class B"

# class C(A,B):
#     varC="welcome to class C"

# c1=C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)





# class car:
#     @staticmethod
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("car stopped")

# class toyottocar(car):
#     def __init__(self,brand):
#         self.brand=brand

# class fortunr(toyottocar):
#     def __init__(self, type):
#         self.type=type

# car1=fortunr("disel")
# car1.start()       







# class teacher:
#     def __init__(self,name,subject):
#         self.name=name
#         self.subject=subject
    
#     def get_name(self):
#         print("Teacher Name:",self.name)
#     def get_subject(self):
#         print("subject Name:",self.subject)

# t1=teacher("sir talha","programming")
# t1.get_name()
# t1.get_subject()




# class student:
#     def __init__(self,name,roll_no,CGPA):
#         self.name=name
#         self.roll_no=roll_no
#         self.CGPA=CGPA
    
#     def get_name(self):
#         print("name",self.name)
#     def get_roll_no(self):
#         print("roll number",self.roll_no)
#     def get_CGPA(self):
#         print("CGPA",self.CGPA)

# s1=student("Javeria Ahmad","8765678","3")
# s1.get_name()
# s1.get_roll_no()
# s1.get_CGPA()







# class acount:             #create acount class with two atributes-balance and acount no   
    
#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.acount_no=acc
# #debit method
#     def debit(self,amount):
#         self.balance-=amount
#         print("RS", amount ,"was debited")
#         print("total amount",self.get_balance())

# #credit method
#     def credit(self,amount):
#         self.balance+=amount
#         print("RS", amount ,"was credited")
#         print("total amount",self.get_balance())
 
#     def get_balance(self):
#         return self.balance

# acc1=acount(10876,45867)
# acc1.debit(1000)
# acc1.credit(500)
















# class car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.cluch=False

#     def start(self):
#        self.cluch=True
#        self.acc=True
#        print("car sarted")

# car1=car()
# car1.start()












# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     @staticmethod
#     def hello():
#         print("hello")
#     def get_avg(self):
#         sum=0
#         for value in self.marks:
#             sum+=value
#         print("hi",self.name,"  your score is",sum/3)

# s1 = student("javeria", [99,98,97])
# s1.get_avg()

# s1.name="ayeshe"
# s1.get_avg()
# s1.hello()



# class user:
#     def __init__(self,username,email,password):
#         self.username=username
#         self.email=email
#         self.password=password

#     def say_hello_to_user(self,user):
#         print(f"sending message to {user.username}:hi {user.username}, its {self.username}") 

# user1=user("javeria","javeri@gmail.com","8765")
# user2=user("anas","anasahmad@gmail.com","45678")

# user1.say_hello_to_user(user2)

# class user:
#     def __init__(self,username,email,password):
#         self.username=username
#         self.email=email
#         self.password=password

#     def say_hi_to_user(self, user):
#          print(f"sending messege to {user.username}:hi {user.username},its {self.username}")

# user1=user("javeria","javeria@gmail.com","1234")
# user2=user("talha","talha@gmail.com","98765")
# user1.say_hi_to_user(user2)