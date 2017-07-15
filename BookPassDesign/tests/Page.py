from lettuce import step, world
from BookPassDesign.classes import Reader, Page


def setup():
    reader = Reader.Reader()


@step("the reader (?P<reader>.{1,64}) has read the page")
def step_impl(step, reader):
    """
    :type step: lettuce.core.Step
    """
    reader.current_book.current_page.position = reader.current_book.current_page.size+1


@step("the reader's (?P<reader>.{1,64}) page is not the last page")
def step_impl(step, reader):
    """
    :type step: lettuce.core.Step
    """
    reader.current_book.current_page = 1


@step("the reader (?P<reader>.{1,64}) should get the next page")
def step_impl(step, reader):
    """
    :type step: lettuce.core.Step
    """
    assert(reader.current_book.current_page == world.a_long_book().get_page(number=2))


@step("a reader (?P<reader>.{1,64}) has a book")
def step_impl(step, reader):
    """
    :type step: lettuce.core.Step
    """
    reader.current_book = world.a_long_book()


@step("a reader (?P<reader>.{1,64}) picks up a new book")
def step_impl(step, reader):
    """
    :type step: lettuce.core.Step
    """
    reader.current_book = world.a_long_book()
    reader.current_book.current_page = 0


@step("the reader (?P<reader>.{1,64}) should be able to pick between the table of contents and bookmarks")
def step_impl(step, reader):
    """
    :type step: lettuce.core.Step
    """
    assert(reader.has_options([
        'table of contents',
        'bookmarks'
    ]))


@step("a reader (?P<reader>.{1,64}) reads the last word of the book")
def step_impl(step, reader):
    """
    :type reader: str
    :type step: lettuce.core.Step
    """
    reader.current_book.current_page = world.a_long_book().size
    reader.current_book.current_page.position = reader.current_book.current_page.size+1