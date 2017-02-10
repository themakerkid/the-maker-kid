"""
Routes and views for The MAKER Kid flask application.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, Blueprint, request, session, url_for
from flask.ext.script import Manager

stem = Blueprint('stem', __name__)

@stem.before_request
def forum_continue():
    session["continue"] = url_for(request.endpoint)

@stem.route('/')
def index():
    """Renders the home page."""
    return render_template('stem/indexDefo.html', title='Home Page', year=datetime.now().year)

@stem.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@stem.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'stem/about.html', 
        title='About Me', 
        year=datetime.now().year
    )

@stem.route('/scratch')
def scratch():
    """Renders the Scratch home page."""
    return render_template('stem/tech/scratch/scratch.html', title='Scratch - Home', year=datetime.now().year)

@stem.route('/scratch/learn')
def scratchLearn():
    """Renders the Scratch learning page."""
    return render_template('stem/tech/scratch/scratchLearn.html', title='Scratch - Learning Resources', year=datetime.now().year)

@stem.route('/scratch/project')
def scratchProject():
    """Renders the Scratch 'Award Winning Project' page."""
    return render_template('stem/tech/scratch/scratchProject.html', title='Scratch - Award Winning Project', year=datetime.now().year, time=datetime.now().year - 2015)

@stem.route('/scratch/project/videos/')
def scratchProjectVideos():
    """Renders the Scratch 'Award Winning Project' video page no.1."""
    return render_template('stem/tech/scratch/scratchProjectVideos.html', title='Scratch - Award Winning Project Videos - Page 1', year=datetime.now().year)

#@stem.route('/scratch/project/videos/2')
#def scratchProjectVideos2():
#    """Renders the Scratch 'Award Winning Project' video page no.2."""
#    return render_template('stem/tech/scratch/scratchProjectVideos2.html', title='Scratch - Award Winning Project Videos - Page 2', year=datetime.now().year)

@stem.route('/processing')
def processing():
    """Renders the khan projects page."""
    return render_template('stem/tech/processing/gettingStarted.html', title="Processing - Getting Started", year=datetime.now().year)

@stem.route('/processing/learn')
def processingLearn():
    """Renders the khan projects page."""
    return render_template('stem/tech/processing/learn.html', title="Processing - Learning Resources", year=datetime.now().year)

@stem.route('/webCoding')
def websiteCoding():
    """Renders the khan projects page."""
    return render_template('stem/tech/websiteCode/gettingStarted.html', title="Website Coding - Home Page", year=datetime.now().year)

@stem.route('/webCoding/learn')
def webCodeLearn():
    """Renders the khan projects page."""
    return render_template('stem/tech/websiteCode/learn.html', title="Website Coding - Learning Resources", year=datetime.now().year)

@stem.route('/webCoding/thisWebsite')
def webCodeThis():
    """Renders the khan projects page."""
    return render_template('stem/tech/websiteCode/thisWebsite.html', title="Website Coding - Learning Resources", year=datetime.now().year)

@stem.route('/raspi')
def raspi():
    """Renders the khan projects page."""
    return render_template('stem/tech/websiteCode/thisWebsite.html', title="Website Coding - Learning Resources", year=datetime.now().year)

@stem.route('/raspi/learn')
def raspiLearn():
    """Renders the khan projects page."""
    return render_template('stem/tech/websiteCode/thisWebsite.html', title="Website Coding - Learning Resources", year=datetime.now().year)

@stem.route('/raspi/python')
def raspiPython():
    """Renders the khan projects page."""
    return render_template('stem/tech/websiteCode/thisWebsite.html', title="Website Coding - Learning Resources", year=datetime.now().year)

@stem.route('/raspi/codeWeb')
def raspiCode():
    """Renders the khan projects page."""
    return render_template('stem/tech/websiteCode/thisWebsite.html', title="Website Coding - Learning Resources", year=datetime.now().year)

@stem.route('/raspi/hardware')
def raspiHardware():
    """Renders the khan projects page."""
    return render_template('stem/tech/websiteCode/thisWebsite.html', title="Website Coding - Learning Resources", year=datetime.now().year)

@stem.route('/processing/khan/drawing')
def drawing():
    """Renders the khan projects page."""
    return render_template('stem/tech/khancode/static_projects.html', title="My Khan Projects", year=datetime.now().year)

@stem.route('/processing/khan/mouseOver')
def mouseOver():
    return render_template('stem/tech/khancode/mouseOverProjects.html', title="Mouse Over Projects", year=datetime.now().year)

@stem.route('/processing/khan/animations')
def animations():
    return render_template('stem/tech/khancode/processingProjects.html', title="Animations", year=datetime.now().year)

@stem.route('/webCoding')
def webCode():
    """Renders the khan projects page."""
    return render_template('stem/tech/wesiteCode/gettingStarted.html', title="Website Coding - Getting Started", year=datetime.now().year)

@stem.route('/maths')
def maths():
    return render_template('stem/maths/mathsHome.html', title="Mathematics - Home Page", year=datetime.now().year)

@stem.route('/maths/famous')
def mathsFamous():
    return render_template('stem/maths/famous2.html', title="Mathematics - Famous Mathematicians", year=datetime.now().year)

@stem.route('/maths/learn')
def mathsLearn():
    return render_template('stem/maths/learning.html', title="Mathematics - Learning Websites", year=datetime.now().year)

@stem.route('/maths/books')
def mathsBooks():
    return render_template('stem/maths/books.html', title="Mathematics - Books", year=datetime.now().year)

@stem.route('/maths/projects')
def mathsProjects():
    return render_template('stem/maths/projects.html', title="Mathematics - My Projects", year=datetime.now().year)

@stem.route('/maths/software')
def mathsSoftware():
    return render_template('stem/maths/software.html', title="Mathematics - Software", year=datetime.now().year)

@stem.route('/maths/competitions')
def mathsComp():
    return render_template('stem/maths/competitions.html', title="Mathematics - Competitions", year=datetime.now().year)

@stem.route('/maths/learnstorm')
def mathsLearnstorm():
    return render_template('stem/maths/learnstorm.html', title="Mathematics - Learnstorm", year=datetime.now().year)

@stem.route('/maths/glossary')
def mathsGlossary():
    return render_template('stem/maths/glossary.html', title="Mathematics - Glossary", year=datetime.now().year)

@stem.route('/starting')
def starting():
    return render_template('stem/science/scienceHome.html', title="Getting Started - Home Page", year=datetime.now().year)

@stem.route('/starting/books')
def sciBooks():
    return render_template('stem/science/books.html', title="Getting Started - Books", year=datetime.now().year)

@stem.route('/starting/events')
def sciCompEvents():
    return render_template('stem/science/compEvent.html', title="Getting Started - Events", year=datetime.now().year)

@stem.route('/starting/glossary')
def sciGlossary():
    return render_template('stem/science/glossary.html', title="Getting Started - Glossary", year=datetime.now().year)

@stem.route('/starting/learn')
def sciLearn():
    return render_template('stem/science/learn.html', title="Getting Started - Learning Resources", year=datetime.now().year)

@stem.route('/starting/famous')
def famous():
    return render_template('stem/tech/technologists.html', title="Getting Started - Famous Makers &amp; Technologists", year=datetime.now().year)

"""
@stem.route('/starting/projects')
def sciProjects():
    return render_template('stem/science/projects.html', title="Getting Started - Projects", year=datetime.now().year)
"""

@stem.route('/starting/scientists')
def sciScientists():
    return render_template('stem/science/scientists.html', title="Getting Started - Famous Scientists", year=datetime.now().year)

@stem.route('/starting/toys')
def sciToys():
    return render_template('stem/science/toys.html', title="Getting Started - Toys", year=datetime.now().year)

@stem.route('/hardware')
def hardware():
    return render_template('stem/eng/engHome.html', title="Hardware - Home Page", year=datetime.now().year)

@stem.route('/hardware/learn')
def engLearn():
    return render_template('stem/eng/learn.html', title="Hardware - Learning Resources", year=datetime.now().year)

@stem.route('/hardware/books')
def engBooks():
    return render_template('stem/eng/books.html', title="Hardware - Books", year=datetime.now().year)

@stem.route('/hardware/engineers')
def engineers():
    return render_template('stem/eng/engineers.html', title="Hardware - Famous Engineers", year=datetime.now().year)

@stem.route('/hardware/electronics')
def engElec():
    return render_template('stem/eng/elec.html', title="Hardware - Electronics - Getting Started", year=datetime.now().year)

@stem.route('/hardware/electronics/arduino')
def engElecArd():
    return render_template('stem/eng/ardBooks.html', title="Hardware - Electronics - Arduino", year=datetime.now().year)

@stem.route('/hardware/robotics')
def engRobot():
    return render_template('stem/eng/robot.html', title="Hardware - Robotics", year=datetime.now().year)

@stem.route('/hardware/projects')
def engProj():
    return render_template('stem/eng/projects.html', title="Hardware - Projects", year=datetime.now().year)

@stem.route('/hardware/toys')
def engToys():
    return render_template('stem/eng/toys.html', title="Hardware - Toys", year=datetime.now().year)

@stem.route('/hardware/competitionsAndEvents')
def engCompEv():
    return render_template('stem/eng/compEv.html', title="Hardware - Compitions & Events", year=datetime.now().year)

@stem.route('/hardware/glossary')
def engGlossary():
    return render_template('stem/eng/glossary.html', title="Hardware - Glossary", year=datetime.now().year)

@stem.route('/coding')
def coding():
    return render_template('stem/tech/techHome.html', title="Coding (Basic) - Introduction", year=datetime.now().year)

@stem.route('/coding/python')
def techPython():
    return render_template('stem/tech/python/gettingStarted.html', title="Technology - Python - Getting Started", year=datetime.now().year)

@stem.route('/coding/python/learn')
def techPyLearn():
    return render_template('stem/tech/python/learn.html', title="Technology - Python - Learning Resources", year=datetime.now().year)

@stem.route('/coding/python/this')
def techPyThis():
    return render_template('stem/tech/python/thisWebsite.html', title="Technology - Python - This Website", year=datetime.now().year)

@stem.route('/coding/eventsCompetitions')
def techEveComp():
    return render_template('stem/tech/eveComp.html', title="Technology - Events & Competitions", year=datetime.now().year)

@stem.route('/coding/glossary')
def techGlossary():
    return render_template('stem/tech/glossary.html', title="Technology - Python - This Website", year=datetime.now().year)

@stem.route('/funstuff/toys')
def otherToys():
    return render_template('stem/coolToys.html', title="Fun Stuff - Cool Toys", year=datetime.now().year)

@stem.route('/ajax/index')
def ajaxIndex():
    return render_template('stem/ajax/example.html', title="Ajax - Timetable", year=datetime.now().year)


@stem.route('/ajax/route')
def ajaxRoute():
    return render_template('stem/ajax/jq-load2.html', title="Ajax - Route", year=datetime.now().year)


@stem.route('/ajax/toys')
def ajaxToys():
    return render_template('stem/ajax/jq-load3.html', title="Ajax - Toys", year=datetime.now().year)


@stem.route('/ajax/home')
def ajaxHome():
    return render_template('stem/ajax/jq-load.html', title="Ajax - Home", year=datetime.now().year)

"""
Probably to be uncommented later:
404 handler
@stem.app_errorhandler(404)
def no_page(e):
    return redirect('/')
"""