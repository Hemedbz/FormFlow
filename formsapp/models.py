from django.db import models
from django.contrib.auth.models import User

class QuestionType(models.Model):
    class Meta:
        db_table = 'question_types'

    question_type = models.CharField()

class Form (models.Model):
    class Meta:
        db_table = 'forms'

    creation_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField(null=True, blank=True)

class Question (models.Model):
    class Meta:
        db_table = 'questions'

    question = models.CharField()
    question_type = models.ForeignKey(QuestionType)

class PossibleAnswer(models.Model):
    class Meta:
        db_table = 'possible_answers'

    question_id = models.ForeignKey(Question)
    possible_answer =


class Answer (models.Model):
    class Meta:
        db_table = 'answers'
        answer_content =
        date =
        answering_user_id =


class Owner(models.Model):
    class Meta:
        db_table = 'owners'
        user_id =
        form_id =


class PossibleAnswer(models.Model):
    class Meta:
        db_table = 'possible_answers'


class FormQuestionLink(models.Model):
    class Meta:
        db_table = 'forms_questions'
        form_id =
        question_id =


class QuestionAnswerLink(models.Model):
    class Meta:
        db_table = 'questions_answers'
        question_id =
        answer_id =