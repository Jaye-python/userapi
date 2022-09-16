# API endpoint to get a list of users

## URLs

This site is hosted on [pythonanywhere](https://olalekanj.pythonanywhere.com/users/) :telescope:

`URL to get users:`  [(https://olalekanj.pythonanywhere.com/users/)]

`URL to seed the DB with 10,000 users at a time:`  [(https://olalekanj.pythonanywhere.com/seeddb/)]

`Swagger Documentation:`  [(https://olalekanj.pythonanywhere.com/api/schema/swagger-ui/)]

`Redocs Documentation:`  [(https://olalekanj.pythonanywhere.com/api/schema/redoc/)]

## Search

You may search by `first_name` or `last_name` which is case inSeNsitive and will return parts of the text that match

`This will return all those whose first name contains 'jo':`

[(https://olalekanj.pythonanywhere.com/users/?first_name__icontains=jo&last_name__icontains=)]

## Pagination

Each page returns 20 records per page

## Caching

Caching is achieved using `Redis` with `Time To Live (TTL)` of 1 minute



