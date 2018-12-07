import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from .careers_types import *

def process_text(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english')).union(set(string.punctuation))
    filtered_words = [w.lower() for w in words if not w.lower() in stop_words]
    return filtered_words

def compare_skills(career, key_words, score, rank_field, ranking):
    career_list = list(career)
    for word in key_words:
        ranking[rank_field] += score * career_list.count(word.lower())

def give_rank(key_words, ranking, score=1):
    #compare with front end    
    compare_skills(front_end, key_words, score, "front-end", ranking) 
    
    #compare with backend
    compare_skills(back_end, key_words, score, "back-end", ranking) 

    #compare with database administration
    compare_skills(database_admin, key_words, score, "database administration", ranking) 

    #compare with desktop application
    compare_skills(desktop_application, key_words, score, "desktop application", ranking) 

    #compare with mobile
    compare_skills(mobile, key_words, score, "mobile", ranking) 

    #compare with graphics
    compare_skills(graphics, key_words, score, "graphics", ranking) 

    #compare with game
    compare_skills(game, key_words, score, "game", ranking) 

    #compare with data science
    compare_skills(data_science, key_words, score, "data science", ranking) 

    #compare with big data
    compare_skills(big_data, key_words, score, "big data", ranking) 

    #compare with devops
    compare_skills(devops, key_words, score, "devops", ranking) 

    #compare with testing
    compare_skills(testing, key_words, score, "testing", ranking) 

    #compare with security
    compare_skills(security, key_words, score, "security", ranking) 

    #compare with embedded
    compare_skills(embedded, key_words, score, "embedded", ranking) 

    #compare with system
    compare_skills(system, key_words, score, "system", ranking) 

def best_three_careers(ranking):
    careers = list(ranking.items())
    careers.sort(key=lambda x:x[1], reverse=True)
    return [x[0] for x in careers[:3]]

def process_resume_data(resume):
    ranking = {
        "front-end": 0,
        "back-end":  0,
        "database administration": 0,
        "desktop application": 0,
        "mobile": 0,
        "graphics": 0,
        "game":  0,
        "data science": 0,
        "big data": 0,
        "devops": 0,
        "testing":  0,
        "security": 0,
        "embedded": 0,
        "system": 0
    }
    education = process_text(resume["education"])
    give_rank(education, ranking)

    work_experience = process_text(resume["work_experience"])
    give_rank(work_experience, ranking, score=5)

    areas_of_interest = process_text(resume["areas_of_interest"])
    give_rank(areas_of_interest, ranking, score=3)

    projects = process_text(resume["projects"])
    give_rank(projects, ranking, score=2)

    technical_skills = process_text(resume["technical_skills"])
    give_rank(technical_skills, ranking)

    publications = process_text(resume["publications"])
    give_rank(publications, ranking, score=2)

    technical_events = process_text(resume["technical_events"])
    give_rank(technical_events, ranking)

    extra_curricular_activities = process_text(resume["extra_curricular_activities"])
    give_rank(extra_curricular_activities, ranking)

    personal_info = process_text(resume["personal_info"])
    give_rank(personal_info, ranking)

    return best_three_careers(ranking)