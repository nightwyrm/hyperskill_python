from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_task():
    new_task = input('Enter task')
    new_deadline = input('Enter deadline')
    session.add(Table(task=new_task, deadline=datetime.strptime(new_deadline, '%Y-%m-%d')))
    session.commit()
    print('The task has been added!\n')


def delete_task():
    print('Choose the number of the task you want to delete:')
    rows = session.query(Table).order_by(Table.deadline).all()
    if len(rows) == 0:
        print('Nothing to do!')
    else:
        for order, row in enumerate(rows):
            print(f"{order + 1}. {row.task}. {datetime.strftime(row.deadline, '%-d %b')}")
    session.delete(rows[int(input()) - 1])
    session.commit()
    print('The task has been deleted!\n')


def print_today():
    print(f"Today {datetime.strftime(datetime.today(), '%d %b')}:")
    rows = session.query(Table).filter(Table.deadline == datetime.today().date()).all()
    if len(rows) == 0:
        print('Nothing to do!')
    else:
        for order, row in enumerate(rows):
            print(order + 1, row.task, sep='. ')
    print('')


def print_week():
    for i in range(7):
        rows = session.query(Table).filter(Table.deadline == (datetime.today() + timedelta(days=i)).date()).all()
        print('\n' + str((datetime.today() + timedelta(days=i)).strftime('%A %d %b')) + ':')
        if len(rows) == 0:
            print('Nothing to do!')
        else:
            for order, row in enumerate(rows):
                print(order + 1, row.task, sep='. ')
    print('')


def print_missed():
    print('Missed tasks:')
    rows = session.query(Table).filter(Table.deadline < datetime.today().date()).all()
    if len(rows) == 0:
        print('Nothing to do!')
    else:
        for order, row in enumerate(rows):
            print(order + 1, row.task, sep='. ')
    print('')


def print_all():
    print('All tasks:')
    rows = session.query(Table).order_by(Table.deadline).all()
    if len(rows) == 0:
        print('Nothing to do!')
    else:
        for order, row in enumerate(rows):
            print(f"{order + 1}. {row.task}. {datetime.strftime(row.deadline, '%-d %b')}")
    print('')


while True:
    print("""1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit""")
    option = input()
    if option == '0':
        exit()
    elif option == '1':
        print_today()
    elif option == '2':
        print_week()
    elif option == '3':
        print_all()
    elif option == '4':
        print_missed()
    elif option == '5':
        add_task()
    elif option == '6':
        delete_task()
