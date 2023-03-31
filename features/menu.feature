Feature: Menu feature

    Background:
      Given home: I am a user on emag.ro Home page

    @tab
    Scenario Outline: Click on item tab
      When menu_tab: I click on <tab_name>
      Then <page_name>: I verify that the url is "https://www.emag.ro/<url_path>"

      Examples:
      |page_name    | tab_name  | url_path              |
      |genius_page  | Genius    | genius?ref=hdr_genius |

