from graphene import Schema, ObjectType, Float, Field
from graphene.types.scalars import Int
import psycopg2

class MyAvgSalary(ObjectType):
    minsalary = Int()
    maxsalary = Float()

class AvgSalaryMonth(ObjectType):
    showavgsal = Field(MyAvgSalary)

    def resolve_showavgsal(self, info):
        try:
            con = psycopg2.connect(database='mycompany', user='postgres',password='Ravi', host='localhost', port=5432)
            cur = con.cursor()
            query = 'select min(salary), max(salary) max from company'
            cur.execute(query,)
            data = cur.fetchall()
            print(data[0][0])
            return MyAvgSalary(minsalary=data[0][0])

        except (Exception, psycopg2.DatabaseError) as error:
            return {'error': error}

class Query(AvgSalaryMonth, ObjectType):
    pass


schema = Schema(query=Query)