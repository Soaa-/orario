# master table id: ctl00_PageBody_tblBodyShow1
from bs4 import BeautifulSoup

def main():
    soup = BeautifulSoup(open('fw2013.html'))
    master = soup.find(id='ctl00_PageBody_tblBodyShow1')
    course_anchors = master('td', style='background-color:Maroon;')
    for anchor in course_anchors:
        course_number = anchor.next_sibling
        course_title = course_number.next_sibling
        course_credits = course_title.next_sibling
        for row in anchor.parent.next_siblings:
            pass

def handle_prereqs(row):
    """ Returns a list of prereqs in the form
        of course numbers.
    """
    pass

def handle_note(row):
    """ Returns a string containing the special
        note.
    """
    pass

def handle_section(row):
    """ Returns a dict containing all the attributes
        of the section.
    """
    pass
    
if __name__ == '__main__':
    main()