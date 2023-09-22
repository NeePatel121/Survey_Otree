from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'survey_app'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Name = models.StringField(label='Enter your Name:')
    Email = models.StringField(label='Enter your Email:')
    Campus_ID = models.LongStringField(label='Enter your Campus ID')
    Exercise = models.StringField(choices=[["I don't know", "I don't know"], ['1-2 days', '1-2 days'], ['3-5 days', '3-5 days'], ['6+ days', '6+ days']], label='How Many Days a week do you do exercise?', widget=widgets.RadioSelect)
    Duration_exercise = models.StringField(choices=[['0-30 mins', '0-30 mins'], ['30-60 mins', '30-60 mins'], ['60-90 mins', '60-90 mins'], ['more than 90 mins ', 'more than 90 mins ']], label='How much Time do you spend for a regular Exercise?', widget=widgets.RadioSelect)    
    Place_exercise = models.StringField(choices=[['Gym', 'Gym'], ['Home', 'Home'], ['Outside Garden', 'Outside Garden'], ['Others', 'Others']], label='Where do you prefer to do Exercise', widget=widgets.RadioSelect)
    Time_exercise = models.StringField(choices=[['Early in the Morning', 'Early in the Morning'], ['In the Middle of the Day', 'In the Middle of the Day'], ['Afternoon', 'Afternoon'], ['Evening', 'Evening']], label='When Do you perfer to do exercise', widget=widgets.RadioSelect)
    
# PAGES
class Home_page(Page):
    form_model = 'player'
    form_fields = ['Name', 'Email']

class Form(Page):
    form_model = 'player'
    form_fields = ['Campus_ID', 'Exercise', 'Duration_exercise', 'Place_exercise', 'Time_exercise']

class Results(Page):
    form_model = 'player'
    

page_sequence = [Home_page, Form, Results]
