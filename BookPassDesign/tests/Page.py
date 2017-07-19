from lettuce import step, world
from BookPassDesign.classes import Reader, Page


@step("the reader has read the page")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.reader.current_book.current_page.position = world.reader.current_book.current_page.size+1


@step("the reader's page is not the last page")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.reader.current_book.current_page = 1


@step("the reader should get the next page")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert(world.reader.current_book.current_page == world.a_long_book().get_page(number=2))


@step("a reader has a book")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.reader.current_book = world.a_long_book()


@step("a reader picks up a new book")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.reader.current_book = world.a_long_book()
    world.reader.current_book.current_page = 0


@step("the reader should be able to pick between the table of contents and bookmarks")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert(world.reader.has_options([
        'table of contents',
        'bookmarks'
    ]))


@step("a reader reads the last word of the book")
def step_impl(step):
    """
    :type reader: str
    :type step: lettuce.core.Step
    """
    world.reader.current_book.current_page = world.a_long_book().size
    world.reader.current_book.current_page.position = world.reader.current_book.current_page.size+1