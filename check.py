state_machine.sorts = {
    'AGENT': ['agent_mikolaj'],
    'BOOLEAN': ['True', 'False'],
    'PERFORMANCE': ['good', 'sufficient', 'unsufficient', 'bad'],
    'LEVEL': ['low', 'medium', 'high'],
    'REAL': []
}



state_machine.predicates = {
    'chance_cardio_disease': ['AGENT', 'BOOLEAN'],
    'alcoholism': ['AGENT', 'REAL'],
    'feeling_of_loneliness': ['AGENT', 'BOOLEAN'],
    'performance_at_work': ['AGENT', 'PERFORMANCE'],
    'training': ['AGENT', 'BOOLEAN'],
    'emotion_regulation_ability': ['AGENT', 'REAL'],
    'social_activities_enjoyed': ['AGENT', 'REAL'],
    'level_of_vulnerability': ['AGENT', 'LEVEL'],
    'expectation_of_others': ['AGENT', 'REAL']
}