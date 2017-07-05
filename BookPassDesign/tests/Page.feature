# Created by nated at 7/2/2017
Feature: Book
  # Enter feature description here
  A contains a table of contents, pages, and bookmarks. The reader should be able to navigate and read pages easily

  Scenario: Switch Page
    Given a reader (?P<reader>.{1,64}) has a book
    And the reader's (?P<reader>.{1,64}) page is not the last page
    And the reader (?P<reader>.{1,64}) has read the page
    Then the reader (?P<reader>.{1,64}) should get the next page

  Scenario: Pick up Book
    Given a reader (?P<reader>.{1,64}) picks up a new book
    Then the reader (?P<reader>.{1,64}) should be able to pick between the table of contents and bookmarks

  Scenario: Reach end of book
    Given a reader (?P<reader>.{1,64}) reads the last word of the book
    Then the reader (?P<reader>.{1,64}) should be able to pick between the table of contents and bookmarks



