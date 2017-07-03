# Created by nated at 7/2/2017
Feature: Book
  # Enter feature description here
  A contains a table of contents, pages, and bookmarks. The reader should be able to navigate and read pages easily

  Scenario: Switch Page
    Given a reader has read a page
    And the page is not the last page
    Then the reader should get the next page

  Scenario: Pick up Book
    Given a reader picks up a book
    Then they should be able to pick between the table of contents and bookmarks

