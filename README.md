# Pickworst

An extremely simple app for seeing who's worst.

Created as an exercise in using Python in conjunction with Sqlite.

The app presents the user with a choice of two people and records who they think is worst.

You can also see who the worst person is, or a list of the 10 worst people overall.

This is all CLI based for now. I might think about adding a very simple web framework at some point.

### Potential future development

Some ideas that might be useful, in no particular order:

1. Validate names as they're added in order to avoid duplicates
1. Check names against a list of ones I don't want to include. (E.g. Adolf Hitler, would always win and come out top, therefore boring.)
1. Add unit tests
1. Add web framework
1. Add ability to display images next to the candidates
1. Stronger validation for user input?
1. Ability to post to Twitter, run polls, collect voting data and incorporate that into the database
