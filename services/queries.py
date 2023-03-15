from sqlalchemy import text

class Query():

    def __init__(self, db) -> None:
        self.db = db

    def get_query_one(self):

        query = text("""
            SELECT 
            departments.department,
            count(*) as num_hired 
            FROM 
            departments 
            JOIN hired_employees ON departments.id = hired_employees.department_id
            GROUP BY 
            departments.department
            """)
        
        result = self.db.execute(query).fetchall()
        output = []
        for row in result:
            output.append({
                "department": row[0],
                "num_hired": row[1]
            })

        return output
    
    def get_query_two(self):

        query = text("""
            SELECT 
            departments.department, 
            COUNT(hired_employees.id) AS num_employees_hired
            FROM departments
            JOIN hired_employees ON departments.id = hired_employees.department_id
            GROUP BY departments.department
            ORDER BY num_employees_hired DESC;
            """)
        
        result = self.db.execute(query).fetchall()
        output = []
        for row in result:
            output.append({
                "department": row[0],
                "num_employees_hired": row[1]
            })

        return output