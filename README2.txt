READ ME - DQB DJANGO APP

(As of beginning of day 12/18/2017)
Basically, the idea at the moment for the django app is to have two sets of data --
 the original data as produced by the OCR in the mongodb database, and then the revised data that will be kept 
 as part of the django database. At the moment the site is very bare bones -- the only 
 reason that it looks a little bit good is because I borrowed some of the html from 
 the Penn's treaty project -- this can certainly be changed, there's no reason why it 
 needs to look the way it does.
 
 At the moment there is a home page, which does nothing, and there is an index that links 
 to pages for different profiles. What I'd like is for that index to link to a profile 
 page for each page of the DQB (which for the most part represents a person, except 
 when a person takes multiple pages). On the profile page, when you first visit it, it 
 will have two halves: on the left, the jpeg of the scanned document. On the right, a 
 form (like the one up there now) that will already be populated with the generated OCR text.
 Then the visitor to the site can go in and edit the text and fill out the other fields 
 of the forms. Once this is done, that person is added to the django database. Then, if you
 visit their profile again, it will just have the information.
 
 In the future, I would like there to be two indexes -- one of pages that have yet to be 
 revised, and one of pages that have already been revised. Then, when the form is submitted
 and the person is added to the database, they get moved from one index to another.