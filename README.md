# EU4 Event Explorer

The purpose of this project is to provide a way of exploring EU4 (Europa Universalis 4) events. The idea came from a discussion on reddit where someone asked how many events there are that affect stability. A simple grep in the events directory could give the answer, but EU4's events are structured in a fairly complex way that is hard to parse with just text search.

This project has two basic parts: a parser and a web app. The parser will go through all events and transform them into XML. The web app will then use this to allow querying the events in XPath, which allows expressing complex relations between event parameters, e.g find all events which can trigger between 1444 and 1500 which will cause stability to increase by 1.

Please note that the web app is currently lacking the functionality to fully use the complex search I'm wanting, and I haven't had time to implement it.
