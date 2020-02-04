import datetime
from database import db_session

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


from models import Department as DepartmentModel
from models import Employee as EmployeeModel
from models import Role as RoleModel
from models import User as UserModel
from models import Questionnaire as QuestionnaireModel
from models import Project as ProjectModel
from models import UserProject as UserProjectModel
from models import ContractValue as ContractValueModel
from models import Milestone as MilestoneModel
from models import MilestoneChanges as MilestoneChangesModel


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )


class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel
        interfaces = (relay.Node, )
        
class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )
        
class Questionnaire(SQLAlchemyObjectType):
    class Meta:
        model = QuestionnaireModel
        interfaces = (relay.Node, )
        
class Project(SQLAlchemyObjectType):
    class Meta:
        model = ProjectModel
        interfaces = (relay.Node, )
        
class UserProject(SQLAlchemyObjectType):
    class Meta:
        model = UserProjectModel
        interfaces = (relay.Node, )
        
class ContractValue(SQLAlchemyObjectType):
    class Meta:
        model = ContractValueModel
        interfaces = (relay.Node, )
        
class Milestone(SQLAlchemyObjectType):
    class Meta:
        model = MilestoneModel
        interfaces = (relay.Node, )
        
class MilestoneChanges(SQLAlchemyObjectType):
    class Meta:
        model = MilestoneChangesModel
        interfaces = (relay.Node, )

class UserAttribute:
    id = graphene.ID()
    username = graphene.String()
    email = graphene.String()
    phone = graphene.String()
    code = graphene.String()
    # CREATED_BY = Column(UUID)
    # UPDATED_BY = Column(UUID)
    # UPDATED_AT = Column(DateTime)
    # CREATED_AT = Column(DateTime)

class CreateUserInput(graphene.InputObjectType, UserAttribute):
    pass

class CreateUser(graphene.Mutation):
    
    class Arguments:
        input = CreateUserInput()
    
    # ok = graphene.Boolean()
    user = graphene.Field(lambda: User)
        
    def mutate(root, info, input):
        user = UserModel(input)
        # ok = graphene.Boolean()
        db_session.add(user)
        db_session.commit()
        
        return CreateUser(user=user)        
        
class ProjectAttribute:
    id = graphene.ID()
    c_project_id = graphene.Int()
    project_name = graphene.String()
    signature_date = graphene.types.datetime.DateTime()
    service_commencement = graphene.types.datetime.DateTime()
    contract_duration_month = graphene.Int()
    contract_value_usd = graphene.Float()
    projected_margin_usd = graphene.Int()
    component_of_bespoke = graphene.Int()
    often_provide_services = graphene.Int()
    is_transition_plan = graphene.Int()
    transition_plan_date = graphene.types.datetime.DateTime()
    is_transition_charges = graphene.Int()
    transition_charges_usd = graphene.Float()
    is_transformation_plan = graphene.Int()
    transformation_plan_start = graphene.types.datetime.DateTime()
    transformation_plan_end = graphene.types.datetime.DateTime()
    kpi_number = graphene.Int()
    service_levels = graphene.Int()
    is_earn_back = graphene.Int()
    is_customer_atisfaction_report = graphene.Int()
    customer_atisfaction_form = graphene.Int()
    governance_type = graphene.Int()
    governance_often = graphene.Int()
    key_personnel = graphene.Int()
    supplier_personnel = graphene.Int()
    customer_personnel = graphene.Int()
    planned_duration_month = graphene.Int()
    negotiations_month = graphene.Int()
    sole_sourced = graphene.Int()
    proposed_period_weeks = graphene.Int()
    actual_period_weeks = graphene.Int()
    is_due_diligence_completed = graphene.Int()
    # CREATED_BY = Column(UUID)
    # UPDATED_BY = Column(UUID)
    # UPDATED_AT = Column(DateTime)
    # CREATED_AT = Column(DateTime)
    
class CreateProjectInput(graphene.InputObjectType, ProjectAttribute):
    pass

class CreateProject(graphene.Mutation):
    project = graphene.Field(lambda: Project)
    
    class Arguments:
        input = CreateProjectInput()
        
    def mutate(self, info, input):
        project = ProjectModel(input)
        db_session.add(project)
        db_session.commit()
        
        return CreateUser(project=project)
    
class ContractValueAttribute:
    id = graphene.ID()
    year = graphene.Int()
    contract_value_usd = graphene.Float()
    project_id = graphene.Int()
    estimated_cost_usd = graphene.Float()
    # CREATED_BY = Column(UUID)
    # UPDATED_BY = Column(UUID)
    # UPDATED_AT = Column(DateTime)
    # CREATED_AT = Column(DateTime)
 
class ContractValueInput(graphene.InputObjectType, ContractValueAttribute):
    pass
 
class CreateContractValue(graphene.Mutation):
    contract_value = graphene.Field(lambda: ContractValue)
    
    class Arguments:
        input = ContractValueInput()
        
    def mutate(self, info, input):
        contract_value = ContractValueModel(input)
        db_session.add(contract_value)
        db_session.commit()
        
        return CreateContractValue(contract_value=contract_value)
 
class QuestionnaireAttribute:
    id = graphene.ID()
    project_id = graphene.Int()
    user_filler = graphene.Int()
    to_date = graphene.types.datetime.DateTime()
    is_transition_completed = graphene.Int()
    is_transition_charges_paied = graphene.Int()
    is_transformation_completed = graphene.Int()
    missed_kpi = graphene.Int()
    missed_service_level = graphene.Int()
    moved_service_level = graphene.Int()
    payable_service_credits = graphene.Int()
    paied_service_credits = graphene.Int()
    is_paied_passed = graphene.Int()
    pay_back = graphene.Float()
    is_customer_satisfaction_report = graphene.Int()
    customer_satisfaction_result = graphene.Int()
    is_governance = graphene.Int()
    is_governance_minute = graphene.Int()
    is_additional_governance = graphene.Int()
    additional_governance_cause = graphene.Int()
    is_formal_notices = graphene.Int()
    formal_notices_about = graphene.Int()
    formal_notices_type = graphene.Int()
    initiated_CCNs = graphene.Int()
    signed_CCNs = graphene.Int()
    signed_CCNs_type = graphene.Int()
    key_personnel_changed = graphene.Int()
    supplier_personnel_changed = graphene.Int()
    customer_personnel_changed = graphene.Int()
    invoiced_charges_usd = graphene.Float()
    is_not_invoiced = graphene.Int()
    # CREATED_BY = Column(UUID)
    # UPDATED_BY = Column(UUID)
    # UPDATED_AT = Column(DateTime)
    # CREATED_AT = Column(DateTime)

class QuestionnaireInput(graphene.InputObjectType, QuestionnaireAttribute):
    pass        

class CreateQuestionnaire(graphene.Mutation):
    questionnaire = graphene.Field(lambda: Questionnaire)
    
    class Arguments:
        input = QuestionnaireInput()
        
    def mutate(self, info, input):
        questionnaire = QuestionnaireModel(input)
        db_session.add(questionnaire)
        db_session.commit()
        
        return CreateQuestionnaire(questionnaire=questionnaire)
    
class UserProjectAttribute:
    id = graphene.Int()
    user_id = graphene.Int()
    project_id = graphene.Int()
    
class UserProjectInput(graphene.InputObjectType, UserProjectAttribute):
    pass 

class CreateUserProject(graphene.Mutation):
    user_project = graphene.Field(lambda: UserProject)
    
    class Arguments:
        input = UserProjectInput()
        
    def mutate(self, info, input):
        user_project = UserProjectModel(input)
        db_session.add(user_project)
        db_session.commit()
        
        return CreateUserProject(user_project=user_project)

class MilestoneAttribute:
    id = graphene.Int()
    type = graphene.Int()
    project_id = graphene.Int()
    is_payment = graphene.Int()
    date = graphene.types.datetime.DateTime()
    charges_usd = graphene.Float()
    is_paied = graphene.Int()
    # CREATED_BY = Column(UUID)
    # UPDATED_BY = Column(UUID)
    # UPDATED_AT = Column(DateTime)
    # CREATED_AT = Column(DateTime)

class MilestoneInput(graphene.InputObjectType, MilestoneAttribute):
    pass 

class CreateMilestone(graphene.Mutation):
    milestone = graphene.Field(lambda: Milestone)
    
    class Arguments:
        input = MilestoneInput()
        
    def mutate(self, info, input):
        milestone = MilestoneModel(input)
        db_session.add(milestone)
        db_session.commit()
        
        return CreateMilestone(milestone=milestone)

class MilestoneChangesAttribute:
    id = graphene.ID()
    milestone_id = graphene.Int()
    questionnaire_id = graphene.Int()
    impact = graphene.Int()
    
class MilestoneChangesInput(graphene.InputObjectType, MilestoneChangesAttribute):
    pass 

class CreateMilestoneChanges(graphene.Mutation):
    milestone_changes = graphene.Field(lambda: MilestoneChanges)
    
    class Arguments:
        input = MilestoneChangesInput()
        
    def mutate(self, info, input):
        milestone_changes = MilestoneChangesModel(input)
        db_session.add(milestone_changes)
        db_session.commit()
        
        return CreateMilestoneChanges(milestone_changes=milestone_changes)

# class CreateProject(graphene.Mutation):
#     class Arguments:
#         project_name = graphene.String(required=True)
#         contract_duration_month = graphene.Int()
#         kpi_number = graphene.Int()
#         is_transition_plan = graphene.Int()
        
#     project = graphene.Field(lambda: Project)
    
#     def mutate(self, info, input):
#         db_session.add(project)
#         db_session.commit()
        
#         return CreateProject(project=project)

class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()
    create_user = CreateUser.Field()
    create_contract_value = CreateContractValue.Field()
    create_questionnaire = CreateQuestionnaire.Field()
    create_user_project = CreateUserProject.Field()
    create_milestone = CreateMilestone.Field()
    create_milestone_changes = CreateMilestoneChanges.Field()
    
    
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allow only single column sorting
    all_employees = SQLAlchemyConnectionField(
        Employee)
    # all_employees = SQLAlchemyConnectionField(
    #     Employee, sort=Employee.sort_argument())
    # Allows sorting over multiple columns, by default over the primary key
    all_roles = SQLAlchemyConnectionField(Role)
    # Disable sorting over this field
    all_departments = SQLAlchemyConnectionField(Department)
    all_users = SQLAlchemyConnectionField(User)
    all_projects = SQLAlchemyConnectionField(Project)
    all_questionnaires = SQLAlchemyConnectionField(Questionnaire)
    all_user_projects = SQLAlchemyConnectionField(UserProject)
    all_contract_values = SQLAlchemyConnectionField(ContractValue)
    all_milestones = SQLAlchemyConnectionField(Milestone)
    all_milestone_changes = SQLAlchemyConnectionField(MilestoneChanges)  


schema = graphene.Schema(query=Query, mutation=Mutation, types=[Department, Employee, Role, User, Project, Questionnaire, UserProject, Milestone, MilestoneChanges, ContractValue])
