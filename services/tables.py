from models.models_tables import Departments, Jobs, HiredEmployees
from schemas.schemas_tables import DepartmentsCreate, JobsCreate, HiredEmployeesCreate

class Tables():

    def __init__(self, db) -> None:
        self.db = db

    def get_departments(self):
        result = self.db.query(Departments).all()
        return result

    def create_department(self, department: DepartmentsCreate):
        new_department = Departments(**department.dict())
        self.db.add(new_department)
        self.db.commit()
        self.db.refresh(new_department)
        return new_department

    def get_jobs(self):
        result = self.db.query(Jobs).all()
        return result

    def create_job(self, job: JobsCreate):
        new_job = Jobs(**job.dict())
        self.db.add(new_job)
        self.db.commit
        self.db.refresh(new_job)
        self.db.close()
        return new_job

    def get_hired_employees(self):
        result = self.db.query(HiredEmployees).all()
        return result

    def create_hired_employee(self, hired_employee: HiredEmployeesCreate):
        new_hired_employee = HiredEmployees(**hired_employee.dict())
        self.db.add(new_hired_employee)
        self.db.commit()
        self.db.refresh(new_hired_employee)
        self.db.close()
        return new_hired_employee