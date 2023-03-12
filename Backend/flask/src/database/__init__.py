from sqlalchemy.ext.declarative import declarative_base
base = declarative_base()

from database.project_assignment_table import Project_Assignment_Table
from database.project_evaluation_table import Project_Evaluation_Table
from database.project_table import Project_Table
from database.team_table import Team_Table
from database.user_table import User_Table
from database.passwords_table import Passwords_Table
from database.improvement_metrics_table import Improvement_Metrics_Table
from database.metric_table import Metric_Table
from database.metric_assignment_table import Metric_Assignment_Table