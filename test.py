from boto.mturk.connection import MTurkConnection
from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer 

ACCESS_ID = "X"
SECRET_KEY = "X"
HOST = 'mechanicalturk.sandbox.amazonaws.com'
 
mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                      aws_secret_access_key=SECRET_KEY,
                      host=HOST)
 
title = 'Prostate cancer cell detection'
description = ('Describe some cells to help us test for cancer cells!')
keywords = 'cancer, rating, comments'
 
ratings =[('Very unhealthy','-2'),
         ('unhealthy','-1'),
         ('Okay','0'),
         ('Healthy','1'),
         ('Very healthy','1')]

#---------------  BUILD OVERVIEW -------------------

overview = Overview()
overview.append_field('Title', 'Test HIT')
'''overview.append(FormattedContent('<a target="_blank"'
                                 ' href="http://www.bbc.co.uk/football">'
                                 ' my favorite football site</a>'))
'''
 
#---------------  BUILD QUESTION 1 -------------------
 
qc1 = QuestionContent()
qc1.append_field('Title','How does this cell look?')
qc1.append_field('Text','Do your best estimate')
qc1.append_field('Binary','<MimeType><Type>image</Type></MimeType><DataURL>https://news.usc.edu/files/2015/02/Prostate_cancer_with_Gleason_pattern_4_low_mag-824x549.jpg</DataURL><AltText></AltText>')
 
fta1 = SelectionAnswer(min=1, max=1,style='dropdown',
                      selections=ratings,
                      type='text',
                      other=False)
 
q1 = Question(identifier='design',
              content=qc1,
              answer_spec=AnswerSpecification(fta1),
              is_required=True)

#---------------  BUILD QUESTION 2 -------------------

qc2 = QuestionContent()
qc2.append_field('Title','Comment on the two pictures shown below')
qc2.append_field('Binary','<MimeType><Type>image</Type></MimeType><DataURL>http://vvnktrm2.web.engr.illinois.edu/research/crowd-cancer/images/g/93.png</DataURL><AltText></AltText>')
qc2.append_field('Binary','<MimeType><Type>image</Type></MimeType><DataURL>http://vvnktrm2.web.engr.illinois.edu/research/crowd-cancer/images/r/35.png</DataURL><AltText></AltText>')

#---------------  BUILD QUESTION 3 -------------------

qc2 = QuestionContent()
qc2.append_field('Title','Comment on the two pictures shown below')
qc2.append_field('Binary','<MimeType><Type>image</Type></MimeType><DataURL>http://vvnktrm2.web.engr.illinois.edu/research/crowd-cancer/images/g/93.png</DataURL><AltText></AltText>')
qc2.append_field('Binary','<MimeType><Type>image</Type></MimeType><DataURL>http://vvnktrm2.web.engr.illinois.edu/research/crowd-cancer/images/r/22.png</DataURL><AltText></AltText>')

#---------------  BUILD QUESTION 4 -------------------

qc2 = QuestionContent()
qc2.append_field('Title','Comment on the two pictures shown below')
qc2.append_field('Binary','<MimeType><Type>image</Type></MimeType><DataURL>http://vvnktrm2.web.engr.illinois.edu/research/crowd-cancer/images/g/93.png</DataURL><AltText></AltText>')
qc2.append_field('Binary','<MimeType><Type>image</Type></MimeType><DataURL>http://vvnktrm2.web.engr.illinois.edu/research/crowd-cancer/images/r/71.png</DataURL><AltText></AltText>')

#---------------  BUILD QUESTION 5 -------------------

qc2 = QuestionContent()
qc2.append_field('Title','Comment on the two pictures shown below')
qc2.append_field('Binary','<MimeType><Type>image</Type></MimeType><DataURL>http://vvnktrm2.web.engr.illinois.edu/research/crowd-cancer/images/g/93.png</DataURL><AltText></AltText>')
qc2.append_field('Binary','<MimeType><Type>image</Type></MimeType><DataURL>http://vvnktrm2.web.engr.illinois.edu/research/crowd-cancer/images/r/16.png</DataURL><AltText></AltText>')


fta2 = FreeTextAnswer()
 
q2 = Question(identifier="comments",
              content=qc2,
              answer_spec=AnswerSpecification(fta2))
 
#---------------  BUILD QUESTION 3 -------------------
 
qc3 = QuestionContent()
qc3.append_field('Title','Your personal comments')
 
fta3 = FreeTextAnswer()
 
q3 = Question(identifier="comments",
              content=qc3,
              answer_spec=AnswerSpecification(fta3))
 
#--------------- BUILD THE QUESTION FORM -------------------
 
question_form = QuestionForm()
question_form.append(overview)
question_form.append(q1)
question_form.append(q2)
question_form.append(q3)

 
#--------------- CREATE THE HIT -------------------
 
mtc.create_hit(questions=question_form,
               max_assignments=1,
               title=title,
               description=description,
               keywords=keywords,
               duration = 60*5,
               reward=0.05)


