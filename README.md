# FantasyBBall

Simple CLI tool to view ESPN Fantasy Basketball league details using the [pandas](https://pypi.org/project/pandas/), [requests](https://pypi.org/project/requests/), and [json](https://docs.python.org/3/library/json.html) libraries.

Using GET requests from [ESPN's hidden and undocumented API](https://fantasy.espn.com/apis/v3/games), with [Steven Morse's article](https://stmorse.github.io/journal/espn-fantasy-v3.html) as a reference.

---

### Initialising

Users must add personal league information into the `data.json` file, filling the `"league_id"`, `"year"`, `"swid"`, and `"espn_s2"` fields.

<br>

**league_id:**

Opening the ESPN Fantasy league on a browser will provide a link containing a parameter with the league_id (e.g. https://fantasy.espn.com/basketball/league?leagueId=1208536511)

Here, the league_id is `1208536511`, and users will have to enter this into the json file as such: `"league_id": "1208536511"`

<br>

**year:**

This is the year of the season that the user wishes to view. 

For the 2022-2023 season: `"year": "2023"` 

For the 2023-2024 season: `"year": "2024"`

<br>

**swid** and **espn_s2:**

Because ESPN Fantasy leagues are usually private, users will have to provide cookies to "login" to the API.

To obtain them, users must enter any ESPN Fantasy page and right-click to Inspect or `Ctrl+Shift+I`.

The cookies will be available in the Network tab (Firefox) after making a request to the page, seen in the Request Headers.

