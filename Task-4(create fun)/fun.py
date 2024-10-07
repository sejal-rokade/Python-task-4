# example 1
def Book(title,author,price):
    print(f'title={title}')
    print(f'author={author}')
    print(f'price={price}')
    return{
        'title':title,
        'author':author,
        'price':price
    }
book1=Book('book1','abc',70)
print(f'book1={book1}')

print()

book2=Book('book2','xyz',100)
print(f'book2={book2}')

print()
print('------')
print()

# example 2
def student(name,age,mob_no,add):
    print(f'name={name}')
    print(f'age={age}')
    print(f'mob_no={mob_no}')
    print(f'add={add}')
    return{
        'name':name,
        'age':age,
        'mob_no':mob_no,
        'add':add
    }

s1=student('s1',20,45678,'add1')
print(f's1={s1}')