## Inspiration
* In the last 10 years conceptual math has taken roots across the country, pushing out rote math instruction; however, there is very little accessible content for students with disabilities online.
* As a teacher who works with students with disabilities, Jessica decided to tackle this problem with her brother Tom through the Microsoft Hackathon opportunity. 
* In order to access independent online practice problems without teacher support, students with disabilities need cues that are repetitive, simple, and match the direct instruction of the teacher.  
* Current online curriculum, such as Kahn Academy, use lengthy answer keys that show how to solve a problem but are often disconnected from the teacher’s approach. Special education students often cannot comprehend those videos and/or examples and skip the explanation sections. The language is simply too complex to navigate on their own. About 90% of students on Jessica’s caseload get stuck on an online assignment until they receive a cue to help them get started. 
* To address this problem, we created SimpleCues, an automatic cueing tool that uses a chatbot to chunk directions in a manner that mimics the language seen directly in the classroom. This tool would increase the independent participation level of Jessica’s students to 70%. 
## What it does
* SimpleCues’ chatbot is a yellow help button at the bottom that the student can click on when they get stuck.  They can ask a formal question or simply write in “I’m confused”.  The program accounts for misspelled words, so phrases such as “halp me” will work. 
* Then, SimpleCues provides an automatic cue (pre programmed by the teacher). The cue provides a set of special education friendly, chunked directions that serve as a quick reminder on how to get started and directly matches the teachers’ instruction. 
* Additionally, SimpleCues provides a hyperlink to a pre-taught teacher example. Students with disabilities need consistent reference materials in order for a mathematical process and concept to enter their long-term memory. With SimpleCues, teachers can easily upload a tailored cue and pre-taught visual reference tools.
* All students would benefit from this built in support through cueing and repetitive visual guides, but special education students actually need these cues in order to access the standard-level curriculum .
## How we built it
* After Jessica shared her problem with Tom, he shared a few technical tools such as chatbot, hyperlinking, and easy teacher input systems that she could use to support her students.  
* Tom and Jessica picked the most recent unit (percentage) and worked to develop a set of problems that included these built-in supports.
* Tom built out the interface and Jessica added in frequently asked questions and comments into SimpleCues.  Jessica also added in teacher cues (in the form of chunked directions) and hyperlinked a visual reference tool, created by the math teacher, Samantha Claveau.
* After an initial draft, Jessica and Tom relooked at the product and tweaked some of the language and coloring so the product was ready to go. 
## Challenges we ran into
* On the product scoping side, adapting Azure tools to a real classroom presented lots of interesting challenges:
    * Often students with disabilities do not have strong spelling skills, so we trained SimpleCues to process misspelled questions.
    * We realized in testing that the students need immediate feedback on whether or not they got the correct answer.  We customized our Django forms and added this feature.
* Technically, there were interesting hurdles for Jessica when inputting curriculum into Django.  Initially, Jessica felt overwhelmed by but by the final version she could see how easily configurable the percentage problems are and how the code is easily adapted for other teacher's curricular needs.  See  `hello/views.py` in the codebase.
## Accomplishments that we're proud of
* We are most proud of SimpleCue’s chatbot. In her inclusion math classroom, Jessica spends most of her time “cueing” students by breaking down information for them into simpler language.  This program will minimize the need for in-person cues by providing students with manageable, scaffolded chunks of instruction, providing a built-in accommodation. Then, Jessica could provide more 1-on-1 support for the 30% of students who need more intensive support to be successful.
## What we learned
* MSFT NLP can be accessible for teachers! Jessica was able to take control of the QNAMaker-backed chatbot and pre-define automated student-facing help dialogues after a 5-10 minute tutorial from Tom.
* Web development does not need to be intimidating. While he’s developed software professionally for years, it’s often incremental work. This was Tom’s first time building a nontrivial webapp from scratch! Azure webapps starter samples made it easy to deploy a functional Python Django app.
* The provided AI Learning path helped us rapidly understand the breadth of the ML tooling available. While we selected the QNAMaker, we are interested in using document/handwriting OCR or the LUIS service in the future.
## What's next for SimpleCues
* Please send any feedback you have to SimpleCues@outlook.com! We’re also interested in starting conversations with early adopter classrooms.
* Jessica will try these tools with her math teacher in their inclusive 7th and 8th grade setting.  Other teachers have also asked if they could use the feature.  
* Iterate on the chatbot’s cueing language based on student questions. 
* Jess will find some more beta testers in other subjects to explore our hypothesis that this functionality should have applications beyond conceptual math.
* We must finish productionizing the app before scaling to a full classroom:
    * Add user account registration and logins so we can authenticate and maintain student status of solved problems, etc.
    * We need to swap out the chatbot access key for a new one, and to manage it outside of the git repo as recommended by the azure docs.
    * Formalize the QNAMaker interface.  We need to allow the teacher to control the Q & A content but we will establish a data handoff and remove the teacher from direct Azure Blades access.
* Next steps and applications
    * Add a light teacher’s admin screen to customize problem sets, and move their specifications into an Azure document database.
    * Right now we only support pass/fail assignments. Adding grading capabilities will help us address broader classroom use cases.

