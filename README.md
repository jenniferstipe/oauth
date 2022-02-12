# Oauth2

## Terminology

| Term  | Definition |
| ------------- | ------------- |
| Resource owner  | person/entity that owns the data (user), example is a facebook account owner  |
| Client  | application like Yelp (or an internal app in an org) that wants to access a user's data  |
| Authorization server | A server that can invoke authorization decisions, like Facebook/Google/PingFederate |
| Resource Server | API or server that actually serves the user data (facebook photos, google contacts, etc) - can sometimes be the same as the Auth server |
| Authorization grant | proves a user has authorized an action (clicked "Yes" in essence) |
| Redirect URI | also called callback url - if the user consents, to which where do I go next? |
| Access token | key used to get into the data from the resource server |
