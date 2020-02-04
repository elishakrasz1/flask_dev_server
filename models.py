from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Numeric,Integer, String, func
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy.orm import backref, relationship


class Department(Base):
    __tablename__ = 'department'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Role(Base):
    __tablename__ = 'roles'
    
    role_id = Column(Integer, primary_key=True)
    name = Column(String)

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    # id = Column(UUID, primary_key=True)
    username = Column(String)
    email = Column(String)
    phone = Column(String)
    code = Column(String)
    # CREATED_BY = Column(UUID)
    # UPDATED_BY = Column(UUID)
    # UPDATED_AT = Column(DateTime)
    # CREATED_AT = Column(DateTime)

class Project(Base):
    __tablename__ = 'project'
    
    id = Column(UUID, primary_key=True)
    c_project_id = Column(String(255))
    project_name = Column(String(255))
    signature_date = Column(TIMESTAMP(precision=6))
    service_commencement = Column(TIMESTAMP(precision=6))
    contract_duration_month = Column(Integer)
    contract_value_usd = Column('contract value_usd', Numeric)
    projected_margin_usd = Column(Numeric(255, 0))
    component_of_bespoke = Column(Integer)
    often_provide_services = Column(Integer)
    is_transition_plan = Column(Integer)
    transition_plan_date = Column(DateTime)
    is_transition_charges = Column(Integer)
    transition_charges_usd = Column(Numeric)
    is_transformation_plan = Column(Integer)
    transformation_plan_start = Column(DateTime)
    transformation_plan_end = Column(DateTime)
    kpi_number = Column(Integer)
    service_levels = Column(Integer)
    is_earn_back = Column(Integer)
    is_customer_atisfaction_report = Column(Integer)
    customer_atisfaction_form = Column(Integer)
    governance_type = Column(Integer)
    governance_often = Column(Integer)
    key_personnel = Column(Integer)
    supplier_personnel = Column(Integer)
    customer_personnel = Column(Integer)
    planned_duration_month = Column(Integer)
    negotiations_month = Column(Integer)
    sole_sourced = Column(Integer)
    proposed_period_weeks = Column(Integer)
    actual_period_weeks = Column(Integer)
    is_due_diligence_completed = Column(Integer)
    # CREATED_BY = Column(UUID)
    # UPDATED_BY = Column(UUID)
    # UPDATED_AT = Column(DateTime)
    # CREATED_AT = Column(DateTime)

class ContractValue(Base):
    __tablename__ = 'contract_value'
    
    id = Column(UUID, primary_key=True)
    year = Column(Integer)
    contract_value_usd = Column(Numeric)
    project_id = Column(ForeignKey('project.id'))
    estimated_cost_usd = Column(Numeric)
    # CREATED_BY = Column(UUID)
    # UPDATED_BY = Column(UUID)
    # UPDATED_AT = Column(DateTime)
    # CREATED_AT = Column(DateTime)

    project = relationship('Project')

class Questionnaire(Base):
    __tablename__ = 'questionnaire'
    
    id = Column(Integer, primary_key=True)
    project_id = Column(ForeignKey('project.id'))
    user_filler = Column(ForeignKey('user.id'))
    to_date = Column(DateTime)
    is_transition_completed = Column(Integer)
    is_transition_charges_paied = Column(Integer)
    is_transformation_completed = Column(Integer)
    missed_kpi = Column(Integer)
    missed_service_level = Column(Integer)
    moved_service_level = Column(Integer)
    payable_service_credits = Column(Integer)
    paied_service_credits = Column(Integer)
    is_paied_passed = Column(Integer)
    pay_back = Column(Numeric)
    is_customer_satisfaction_report = Column(Integer)
    customer_satisfaction_result = Column(Integer)
    is_governance = Column(Integer)
    is_governance_minute = Column(Integer)
    is_additional_governance = Column(Integer)
    additional_governance_cause = Column(Integer)
    is_formal_notices = Column(Integer)
    formal_notices_about = Column(Integer)
    formal_notices_type = Column(Integer)
    initiated_CCNs = Column(Integer)
    signed_CCNs = Column(Integer)
    signed_CCNs_type = Column(Integer)
    key_personnel_changed = Column(Integer)
    supplier_personnel_changed = Column(Integer)
    customer_personnel_changed = Column(Integer)
    invoiced_charges_usd = Column(Numeric)
    is_not_invoiced = Column(Integer)
    # CREATED_BY = Column(UUID)
    # UPDATED_BY = Column(UUID)
    # UPDATED_AT = Column(DateTime)
    # CREATED_AT = Column(DateTime)
    project = relationship('Project')
    user = relationship('User')
    
class UserProject(Base):
    __tablename__ = 'user_project'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.id'))
    project_id = Column(ForeignKey('project.id'))
    # CREATED_BY = Column(UUID)
    # UPDATED_BY = Column(UUID)
    # UPDATED_AT = Column(DateTime)
    # CREATED_AT = Column(DateTime)
    project = relationship('Project')
    user = relationship('User')


class Milestone(Base):
    __tablename__ = 'milestone'
    
    id = Column(UUID, primary_key=True)
    type = Column(Integer)
    project_id = Column(ForeignKey('project.id'))
    is_payment = Column(Integer)
    date = Column(DateTime)
    charges_usd = Column(Numeric)
    is_paied = Column(ForeignKey('questionnaire.id'))
    # CREATED_BY = Column(UUID)
    # UPDATED_BY = Column(UUID)
    # UPDATED_AT = Column(DateTime)
    # CREATED_AT = Column(DateTime)

    questionnaire = relationship('Questionnaire')
    project = relationship('Project')
    
class MilestoneChanges(Base):
    __tablename__ = 'milestone_changes'
    
    id = Column(UUID, primary_key=True)
    milestone_id = Column(ForeignKey('milestone.id'))
    questionnaire_id = Column(ForeignKey('questionnaire.id'))
    impact = Column(Integer)
    # CREATED_BY = Column(UUID)
    # UPDATED_BY = Column(UUID)
    # UPDATED_AT = Column(DateTime)
    # CREATED_AT = Column(DateTime)
    
    questionnaire = relationship('Questionnaire')
    milestone = relationship('Milestone')

    
class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Use default=func.now() to set the default hiring time
    # of an Employee to be the current time when an
    # Employee record was created
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    role_id = Column(Integer, ForeignKey('roles.role_id'))
    # Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
    department = relationship(
        Department,
        backref=backref('employees',
                        uselist=True,
                        cascade='delete,all'))
    role = relationship(
        Role,
        backref=backref('roles',
                        uselist=True,
                        cascade='delete,all'))
